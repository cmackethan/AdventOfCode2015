import sys
import time

def preProcess(file) -> list[str]:
    p: list[str] = []
    s = file.readlines()[0]
    for c in s:
        if c == 'i' or c == 'o' or c == 'l':
            c = chr(ord(c) + 1)
        p.append(c)
    return p

def passwordIsValid(p: list[str]) -> bool:
    cond1: bool = False
    cond2: bool = False
    firstPair: str = ''
    for i in range(len(p)):
        if not cond1 and i + 2 < len(p) and ord(p[i]) == ord(p[i + 1]) - 1 \
                                        and ord(p[i + 1]) == ord(p[i + 2]) - 1:
            cond1 = True
        if not cond2 and ((i + 2 < len(p) and p[i] == p[i + 1] and p[i + 1] != p[i + 2]) \
           or (i + 1 == len(p) - 1 and p[i] == p[i + 1])) \
           and p[i:i+1] != firstPair:
            if firstPair != '':
                cond2 = True
            else:
                firstPair = p[i] + p[i + 1]
        if cond1 and cond2:
            return True
    return False
    
def nextPassword(s: list[str]) -> list[str]:
    i = len(s) - 1
    while i >= 0 and s[i] == 'z':
        s[i] = 'a'
        i -= 1
    s[i] = chr(ord(s[i]) + 1)
    if s[i] == 'i' or s[i] == 'o' or s[i] == 'l':
        s[i] = chr(ord(s[i]) + 1)
    return s

def solveOne(p: list[str]) -> list[str]:
    while not passwordIsValid(p):
        p = nextPassword(p)
    return p

def solve(file):
    p = preProcess(file)
    p = solveOne(p)
    p1 = ''.join(p)
    p = nextPassword(p)
    p2 = ''.join(solveOne(p))
    return p1 + '\n' + p2

start_time = time.time()
file = open(sys.argv[1], 'r')
print(solve(file))
file.close()
print("--- %s seconds ---" % (time.time() - start_time))