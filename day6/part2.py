import sys
import time
import re

class Instruction:
    def __init__(self, command: str, r1: list[str], r2: list[str]):
        self.command = command
        self.r1x = int(r1[0])
        self.r1y = int(r1[1])
        self.r2x = int(r2[0])
        self.r2y = int(r2[1])

def sumGrid(grid: list[list[int]]) -> int:
    sum = 0
    for row in grid:
        for cell in row:
            print(cell, end=' ')
            sum += cell
        print()
    return sum

def updateGrid(grid: list[list[int]], instr: Instruction) -> list[list[int]]:
    if instr.command == 'turn on':
        for i in range(instr.r1y, instr.r2y + 1):
            for j in range(instr.r1x, instr.r2x + 1):
                grid[i][j] += 1
    elif instr.command == 'turn off':
        for i in range(instr.r1y, instr.r2y + 1):
            for j in range(instr.r1x, instr.r2x + 1):
                if grid[i][j] > 0:
                    grid[i][j] -= 1
    elif instr.command == 'toggle':
        for i in range(instr.r1y, instr.r2y + 1):
            for j in range(instr.r1x, instr.r2x + 1):
                grid[i][j] += 2
    else:
        print(instr.command)
    return grid

def solve(file):
    grid: list[list[int]] = [[0 for i in range(1000)] for j in range(1000)]
    for line in open(file, 'r'):
        line = line.strip()
        command = re.split(' [0-9]', line)[0]
        r1 = re.search('[0-9]*,[0-9]*(?= through)', line).group()
        r2 = re.search('[0-9]*,[0-9]*$', line).group()
        instruction = Instruction(command, r1.split(','), r2.split(','))
        grid = updateGrid(grid, instruction)
    return sumGrid(grid)

start_time = time.time()
print(solve(sys.argv[1]))
print("--- %s seconds ---" % (time.time() - start_time))