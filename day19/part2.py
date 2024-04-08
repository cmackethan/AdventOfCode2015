import sys
import time

class Fabricator:
    def __init__(self, file):
        self.replacements: dict[str, list[str]] = dict()
        end: bool = False
        for line in file:
            if end == True:
                self.molecule: str = line.strip(); break
            if line == '\n':
                end = True; continue
            line = line.strip().split(' => ')
            if line[0] in self.replacements:
                self.replacements[line[0]].append(line[1])
            else:
                self.replacements.update({line[0]: [line[1]]})

    def getMolecule(self, i, len: int, replacement) -> str:
        return self.molecule[:i] + replacement + self.molecule[i + len:]

    def fabricate(self) -> int:
        # Enumerate all possible series of steps to get to the molecule?

def solve(file):
    return Fabricator(file).fabricate()

start_time = time.time()
file = open(sys.argv[1], 'r')
print(solve(file))
file.close()
print("--- %s seconds ---" % (time.time() - start_time))