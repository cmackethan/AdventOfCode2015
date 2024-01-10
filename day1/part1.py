import sys
import time

def solve(file) -> int:
    instructions = open(file, 'r').readlines()[0]
    floor = 0
    for instruction in instructions:
        if instruction == '(':
            floor += 1
        else:
            floor -= 1
    return floor

start_time = time.time()
print(solve(sys.argv[1]))
print("--- %s seconds ---" % (time.time() - start_time))