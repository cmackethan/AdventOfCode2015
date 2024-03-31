import sys
import time
from typing_extensions import Self

GRID_SIZE: int = 100
NUM_STEPS: int = 100
LIGHT_ON: str = '#'
LIGHT_OFF: str = '.'

class Grid:
    def __init__(self):
        self.grid: list[list[Light]] = [[Light() for i in range(GRID_SIZE)] for j in range(GRID_SIZE)]

    def initFromFile(self, file) -> Self:
        for i, row in enumerate(file):
            row = row.strip()
            for j, light in enumerate(row):
                self.grid[i][j].setState(light)
        return self

    def print(self):
        for row in self.grid:
            for light in row:
                print(light.getState(), end=' ')
            print()
        print()

    def printLikeInput(self):
        for row in self.grid:
            for light in row:
                if light.getState() == 1:
                    print(LIGHT_ON, end='')
                else:
                    print(LIGHT_OFF, end='')
            print()
        print()

    def setLight(self, y: int, x: int, light):
        self.grid[y][x] = light

    def getLight(self, y: int, x: int):
        if y < 0 or y >= len(self.grid):
            return Light()
        if x < 0 or x >= len(self.grid[y]):
            return Light()
        return self.grid[y][x]

    def getNextState(self) -> Self:
        next_grid = Grid()
        for i, row in enumerate(self.grid):
            for j, light in enumerate(row):
                next_grid.setLight(i, j, light.getNextState(self, i, j))
        return next_grid
    
    def countLights(self) -> int:
        count: int = 0
        for row in self.grid:
            for light in row:
                count += light.getState()
        return count

class Light:
    def __init__(self):
        self.state: int = 0

    def setState(self, state: str):
        if state == LIGHT_ON:
            self.state = 1
        else:
            self.state = 0

    def getState(self) -> int:
        return self.state
    
    def countNeighbors(self, grid, y: int, x: int) -> int:
        count: int = 0
        for i in range(y - 1, y + 2):
            for j in range(x - 1, x + 2):
                if i == y and j == x:
                    continue
                count += grid.getLight(i, j).getState()
        return count
    
    def getNextState(self, grid, y: int, x: int) -> Self:
        next_light = Light()
        num_neighbors_on: int = self.countNeighbors(grid, y, x)
        if self.getState() == 0 and num_neighbors_on == 3:
            next_light.setState(LIGHT_ON)
        elif self.getState() == 1 and ( num_neighbors_on == 2 or num_neighbors_on == 3 ):
            next_light.setState(LIGHT_ON)
        return next_light

def solve(file):
    grid = Grid().initFromFile(file)
    # grid.printLikeInput()
    for i in range(NUM_STEPS):
        grid = grid.getNextState()
        # grid.printLikeInput()
    return grid.countLights()

start_time = time.time()
file = open(sys.argv[1], 'r')
print(solve(file))
file.close()
print("--- %s seconds ---" % (time.time() - start_time))