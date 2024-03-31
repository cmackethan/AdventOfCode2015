import sys
import time

duration: int = 2503

class Reindeer:
    def __init__(self, name: str, speed: int, time_flying: int, time_resting: int):
        self.name: int = name
        self.speed: int = speed
        self.time_flying: int = time_flying
        self.time_resting: int = time_resting
        self.current_distance: int = 0
        self.points: int = 0

    def setDistance(self, duration: int) -> int:
        if duration == 0: return 0
        interval_len: int = int(self.time_flying) + int(self.time_resting)
        num_intervals: int = int(duration / interval_len)
        time_remaining: int = int(duration) - int(num_intervals * interval_len)
        distance_1: int = int(self.speed) * int(num_intervals) * int(self.time_flying)
        distance_2: int = int(self.speed) * int(min(time_remaining, int(self.time_flying)))
        self.current_distance = distance_1 + distance_2
        return self.current_distance

    def toString(self) -> str:
        return 'name: ' + self.name + ', speed: ' + self.speed + ', time flying: ' \
            + self.time_flying + ', time resting: ' + self.time_resting
    
def calculatePoints(competitors: list[Reindeer], duration: int) -> int:
    max_distance = 0
    for second in range(1, duration + 1):
        # Get max distance
        for reindeer in competitors:
            this_distance = reindeer.setDistance(second)
            if this_distance > max_distance:
                max_distance = this_distance
        # Assign points
        for reindeer in competitors:
            if reindeer.current_distance == max_distance:
                reindeer.points += 1
    max_points = 0
    # Get max pointss
    for reindeer in competitors:
        if reindeer.points > max_points:
            max_points = reindeer.points
    return max_points

def solve(file) -> int:
    competitors: list[Reindeer] = list()
    for line in file:
        line = line.strip().split()
        competitors.append(Reindeer(line[0], line[3], line[6], line[13]))

    return calculatePoints(competitors, duration)

start_time = time.time()
file = open(sys.argv[1], 'r')
print(solve(file))
file.close()
print("--- %s seconds ---" % (time.time() - start_time))