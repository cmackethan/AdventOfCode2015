import sys
import time
from itertools import permutations
import math

class DistanceMap:
    def __init__(self, file):
        self.m: dict[str, dict[str, int]] = {}
        for line in file:
            line = line.strip().split()
            if line[0] in self.m:
                self.m[line[0]].update({line[2]: line[4]})
            else:
                self.m.update({line[0]: {line[2]: line[4]}})
            if line[2] in self.m:
                self.m[line[2]].update({line[0]: line[4]})
            else:
                self.m.update({line[2]: {line[0]: line[4]}})

    def print(self):
        for entry in self.m:
            print(entry, end=': ')
            for t in self.m[entry]: print(t + ': ' + self.m[entry][t], end=', ')
            print()

    def getDistance(self, l1: str, l2: str) -> int:
        return int(self.m[l1][l2])

def solve(file):
    dm = DistanceMap(file)
    dm.print()
    locations = [location for location in dm.m]
    min_total_dist = math.inf
    for i, p in enumerate(permutations(locations)):
        if i > math.perm(len(locations)) / 2:
            break
        total_dist: int = 0
        for j in range(1, len(p)):
            dist = dm.getDistance(p[j - 1], p[j])
            total_dist += dist
        min_total_dist = min(min_total_dist, total_dist)
    return min_total_dist

start_time = time.time()
file = open(sys.argv[1], 'r')
print(solve(file))
file.close()
print("--- %s seconds ---" % (time.time() - start_time))