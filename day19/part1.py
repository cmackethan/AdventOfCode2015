import sys
import time

class Calibrator:
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

    def calibrate(self) -> int:
        molecules: set[str] = set()
        for i, c in enumerate(self.molecule):
            # Single character replacment
            if c in self.replacements:
                for replacement in self.replacements[c]:
                    molecules.add(self.getMolecule(i, 1, replacement))
            # Double character replacement
            if i < len(self.molecule) - 1 and self.molecule[i + 1].islower() \
                and self.molecule[i:i + 2] in self.replacements:
                for replacement in self.replacements[self.molecule[i: i + 2]]:
                    molecules.add(self.getMolecule(i, 2, replacement))
        return len(molecules)

def solve(file):
    return Calibrator(file).calibrate()

start_time = time.time()
file = open(sys.argv[1], 'r')
print(solve(file))
file.close()
print("--- %s seconds ---" % (time.time() - start_time))