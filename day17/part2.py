import sys
import time
import itertools
import math

liters: int = 150
containers: list[int] = list()

def solve(file):
    for line in file:
        containers.append(int(line.strip()))
    min_combo_len: int = math.inf
    num_ways: int = 0
    for i in range(len(containers)):
        combinations = list(itertools.combinations(containers, i))
        for combo in combinations:
            if i > min_combo_len:
                continue
            sum: int = 0
            for container in combo:
                sum += int(container)
            if sum == liters:
                if i < min_combo_len:
                    min_combo_len = i
                    num_ways = 1
                else:
                    num_ways += 1
    return num_ways

start_time = time.time()
file = open(sys.argv[1], 'r')
print(solve(file))
file.close()
print("--- %s seconds ---" % (time.time() - start_time))