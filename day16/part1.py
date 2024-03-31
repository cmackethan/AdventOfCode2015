import sys
import time

tape = dict()

def loadTape(file):
    for line in file:
        line = line.strip().split()
        tape.update({line[0].split(':')[0]: line[1]})

def solve(file):
    for line in file:
        found: bool = True
        line: list = line.strip().split()
        num: int = line[1].split(':')[0]
        i: int = 2
        while i < len(line):
            attr_name: str = line[i].split(':')[0]
            attr_val: int = line[i + 1].split(',')[0]
            if attr_name in tape and attr_val != tape.get(attr_name):
                found = False
            i += 2
        if found == True:
            return num

start_time = time.time()

input2 = open(sys.argv[2], 'r')
loadTape(input2)
input2.close()

file = open(sys.argv[1], 'r')
print(solve(file))
file.close()

print("--- %s seconds ---" % (time.time() - start_time))