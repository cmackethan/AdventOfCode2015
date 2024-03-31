import sys
import time

def getPairings(file) -> list[tuple[frozenset[str], int]]:
    p = {}
    for line in file:
        line = line.replace('.', '').strip().split()
        name1 = line[0]
        name2 = line[-1]
        if line[2] == 'gain':
            happiness = int(line[3])
        else:
            happiness = int(line[3]) * -1
        if frozenset({name1, name2}) in p:
            p[frozenset({name1, name2})] += happiness
        else:
            p.update({frozenset({name1, name2}): happiness})
    return sorted(p.items(), key=lambda x: x[1], reverse=True)

def solve(file):
    # Dinner table is always a circle
    # Everyone always has 2 people sitting next to them
    # Total possible number of arrangements: (n-1)!
    # Our example: 4 people, 3! = 6 possible arrangements
    # First find optimum arrangement,
    # then try less optimum ones until it is possible?

    pairings = getPairings(file)
    dh: int = 0
    # This is not realistic...
    # for i in range(4):
    #     dh += pairings[i][1]
    # print(dh)

    # while arrangementIsInvalid():
    #     rearrange()
    return pairings

start_time = time.time()
file = open(sys.argv[1], 'r')
print(solve(file))
file.close()
print("--- %s seconds ---" % (time.time() - start_time))