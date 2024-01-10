import sys
import time

def solve(file: str) -> int:
    input: str = open(file, 'r').readlines()[0]
    currentPos: tuple[int, int] = (0, 0)
    m: set = { currentPos }
    for move in input:
        if move == '^':
            currentPos = (currentPos[0], currentPos[1] + 1)
        elif move == 'v':
            currentPos = (currentPos[0], currentPos[1] - 1)
        elif move == '>':
            currentPos = (currentPos[0] + 1, currentPos[1])
        elif move == '<':
            currentPos = (currentPos[0] - 1, currentPos[1])
        m.add(currentPos)
    return len(m)

start_time = time.time()
print(solve(sys.argv[1]))
print("--- %s seconds ---" % (time.time() - start_time))