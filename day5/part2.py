import sys
import time
import re

def isNice(string: str) -> int:
    cond1: bool = False
    cond2: bool = False
    m: dict[str, int] = {}
    for i in range(len(string) - 1):
        substr: str = string[i] + string[i + 1]
        j: int = m.get(substr)
        if j != None and j != i - 1:
            cond1 = True
        elif j != i - 1:
            m.update({substr: i})
        if i < len(string) - 2 and string[i] == string[i + 2]:
            cond2 = True
        if cond1 and cond2:
            return 1
    return 0

def solve(file):
    input = open(file, 'r')
    sum: int = 0
    for string in input:
        sum += isNice(string.strip())
    return sum

start_time = time.time()
print(solve(sys.argv[1]))
print("--- %s seconds ---" % (time.time() - start_time))