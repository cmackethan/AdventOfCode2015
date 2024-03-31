import sys
import time
import itertools

liters: int = 150
containers: list[int] = list()

def solve(file):
    for line in file:
        containers.append(int(line.strip()))
    num_ways: int = 0
    for i in range(len(containers)):
        combinations = list(itertools.combinations(containers, i))
        for combo in combinations:
            sum: int = 0
            for container in combo:
                sum += int(container)
            if sum == liters:
                num_ways += 1
    return num_ways

start_time = time.time()
file = open(sys.argv[1], 'r')
print(solve(file))
file.close()
print("--- %s seconds ---" % (time.time() - start_time))