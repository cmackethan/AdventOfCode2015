import sys
import time

class Reindeer:
    def __init__(self, name: str, speed: int, time_flying: int, time_resting: int):
        self.name: int = name
        self.speed: int = speed
        self.time_flying: int = time_flying
        self.time_resting: int = time_resting

    def getDistance(self, duration: int) -> int:
        interval_len: int = int(self.time_flying) + int(self.time_resting)
        num_intervals: int = int(duration / interval_len)
        time_remaining: int = int(duration) - int(num_intervals * interval_len)
        distance_1: int = int(self.speed) * int(num_intervals) * int(self.time_flying)
        distance_2: int = int(self.speed) * int(min(time_remaining, int(self.time_flying)))
        return distance_1 + distance_2

    def toString(self) -> str:
        return 'name: ' + self.name + ', speed: ' + self.speed + ', time flying: ' \
            + self.time_flying + ', time resting: ' + self.time_resting
    
def getMaxDistance(competitors: list[Reindeer]) -> int:
    max_distance: int = 0
    for reindeer in competitors:
        this_distance = reindeer.getDistance(duration)
        max_distance = max(max_distance, this_distance)
    return max_distance

def solve(file) -> Reindeer:
    competitors: list[Reindeer] = list()
    for line in file:
        line = line.strip().split()
        competitors.append(Reindeer(line[0], line[3], line[6], line[13]))

    return getMaxDistance(competitors)

start_time = time.time()
file = open(sys.argv[1], 'r')
print(solve(file))
file.close()
print("--- %s seconds ---" % (time.time() - start_time))