import sys
import time

def nextSequence(n: int, s: str) -> int:
    slen = len(s)
    if n == 0:
        return slen
    output: str = ''
    if slen == 1: return nextSequence(n - 1, '1' + s[0])
    i = 0
    while i < slen:
        count = 1
        while i + 1 < slen and s[i + 1] == s[i]:
            count += 1
            i += 1
        output += str(count) + s[i]
        i += 1
    return nextSequence(n - 1, output)

def solve(file):
    input = file.readlines()[0].strip()
    return nextSequence(50, input)

start_time = time.time()
file = open(sys.argv[1], 'r')
print(solve(file))
file.close()
print("--- %s seconds ---" % (time.time() - start_time))