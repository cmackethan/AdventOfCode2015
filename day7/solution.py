import sys
import time

class Instruction:

    def __init__(self, line: str):
        self.inputs: list[str] = []
        self.output = line[1]
        lh = line[0].split()
        if len(lh) == 1:
            self.operation = 'ASSIGN'
            self.inputs.append(lh[0])
        elif len(lh) == 2:
            self.operation = 'NOT'
            self.inputs.append(lh[1])
        elif len(lh) == 3:
            self.operation = lh[1]
            self.inputs.append(lh[0])
            self.inputs.append(lh[2])

    def toString(self) -> str:
        if len(self.inputs) > 1:
            return self.operation + ' ' + self.inputs[0] + ' ' +  self.inputs[1] + ' -> ' + self.output
        return self.operation + ' ' + self.inputs[0] + ' -> ' + self.output

def readInstruction(m: dict[str, int], op: str, inputs: list[str]) -> (bool, int):

    inputs_have_signal: bool = False
    signal: int = 0

    if op == 'ASSIGN':
        inputs_have_signal = inputs[0].isdigit() or inputs[0] in m
        if inputs_have_signal:
            if inputs[0].isdigit():
                signal = int(inputs[0])
            else:
                signal = m[inputs[0]]
    elif op == 'NOT':
        inputs_have_signal = inputs[0] in m
        if inputs_have_signal:
            signal = 65536 + ~m[inputs[0]]
    elif op == 'AND':
        inputs_have_signal = inputs[1] in m and (inputs[0] in m or inputs[0].isdigit())
        if inputs_have_signal:
            if inputs[0].isdigit():
                signal = int(inputs[0]) & m[inputs[1]]
            else:
                signal = m[inputs[0]] & m[inputs[1]]
    elif op == 'OR':
        inputs_have_signal = inputs[1] in m and inputs[0] in m
        if inputs_have_signal:
            signal = m[inputs[0]] | m[inputs[1]]
    elif op == 'LSHIFT':
        inputs_have_signal = inputs[0] in m
        if inputs_have_signal:
            signal = m[inputs[0]] << int(inputs[1])
    elif op == 'RSHIFT':
        inputs_have_signal = inputs[0] in m
        if inputs_have_signal:
            signal = m[inputs[0]] >> int(inputs[1])

    return (inputs_have_signal, signal)

# "A gate provides no signal until all of its inputs have a signal..."
def sim(m: dict[str, int], qd: dict[str, list[Instruction]], instr: Instruction, inputs_have_signal: bool, signal: int):

    if not inputs_have_signal:
        (inputs_have_signal, signal) = readInstruction(m, instr.operation, instr.inputs)

    if inputs_have_signal:
        m.update({instr.output: signal}) # execute instruction
        if instr.output in qd:
            for i in qd[instr.output]: # for each instruction with instr.output as input
                (inputs_have_signal, signal) = readInstruction(m, i.operation, i.inputs)
                if inputs_have_signal:
                    sim(m, qd, i, inputs_have_signal, signal)
            qd.pop(instr.output) # dequeue
    else:
        for i in instr.inputs: # enqueue
            if i.isdigit():
                continue
            if i in qd:
                qd[i].append(instr)
            else:
                qd.update({i: [instr]})

def solve(file):

    m: dict[str, int] = dict()
    qd: dict[str, list[Instruction]] = dict()

    for line in open(file, 'r'):
        instr = Instruction(line.strip().split(' -> '))
        sim(m, qd, instr, False, 0)

    for wire in sorted(m):
        print(wire + ': ' + str(m[wire]))

    for entry in qd:
        print(entry, end=': ')
        for i in qd[entry]:
            print(i.toString(), end=', ')
        print()

start_time = time.time()
print(solve(sys.argv[1]))
print("--- %s seconds ---" % (time.time() - start_time))