import sys
import time
import re

def isNice(string: str) -> int:
    if re.search('ab|cd|pq|xy', string):
        return 0
    
    numVowels: int = 0
    rep: bool = False
    for i, c in enumerate(string):
        if c in {'a', 'e', 'i', 'o', 'u'}:
            numVowels += 1
        if rep == False and i < len(string) - 1 and string[i + 1] == c:
            rep = True
        if numVowels > 2 and rep == True:
            return 1
    return 0

def solve(file):
    input = open(file, 'r')
    sum: int = 0
    for string in input:
        sum += isNice(string)
    return sum

start_time = time.time()
print(solve(sys.argv[1]))
print("--- %s seconds ---" % (time.time() - start_time))