import sys
import time

def solve(file) -> int:
    instructions = open(file, 'r').readlines()[0]
    floor = 0
    for i, instruction in enumerate(instructions, 1):
        if instruction == '(':
            floor += 1
        else:
            floor -= 1
        if floor == -1:
            return i
    return -1

start_time = time.time()
print(solve(sys.argv[1]))
print("--- %s seconds ---" % (time.time() - start_time))