import sys
import time

def solve(file: str) -> int:
    input: str = open(file, 'r').readlines()[0]
    currentPos: tuple[int, int] = (0, 0)
    santaPos: tuple[int, int] = (0, 0)
    roboPos: tuple[int, int] = (0, 0)
    m: set = { currentPos }
    for i, move in enumerate(input):
        if i % 2 == 0:
            currentPos = santaPos
        else:
            currentPos = roboPos
        if move == '^':
            currentPos = (currentPos[0], currentPos[1] + 1)
        elif move == 'v':
            currentPos = (currentPos[0], currentPos[1] - 1)
        elif move == '>':
            currentPos = (currentPos[0] + 1, currentPos[1])
        elif move == '<':
            currentPos = (currentPos[0] - 1, currentPos[1])
        m.add(currentPos)
        if i % 2 == 0:
            santaPos = currentPos
        else:
            roboPos = currentPos
    return len(m)

start_time = time.time()
print(solve(sys.argv[1]))
print("--- %s seconds ---" % (time.time() - start_time))