import sys
import time

def oldPassword(file) -> list[str]:
    p: list[str] = []
    s = file.readlines()[0]
    return [c for c in s]

def hasSequence(we_know: bool, p: list[str], i: int) -> bool:
    if we_know: return True
    return i + 2 < len(p) and ord(p[i]) == ord(p[i + 1]) - 1 \
                          and ord(p[i + 1]) == ord(p[i + 2]) - 1

def hasTwoPairs(we_know: bool, firstPair: str, p: list[str], i: int) -> (bool, str):
    if we_know: return (True, '')
    if ((i + 2 < len(p) and p[i] == p[i + 1] and p[i + 1] != p[i + 2]) \
           or (i + 1 == len(p) - 1 and p[i] == p[i + 1])) \
           and p[i:i+1] != firstPair:
        if firstPair == '': return (False, p[i] + p[i + 1])
        else: return (True, '')
    return (False, firstPair)

def passwordIsValid(p: list[str]) -> bool:
    conds: list[bool] = [False] * 2
    first_pair: str = ''
    for i in range(len(p)):
        conds[0] = hasSequence(conds[0], p, i)
        (conds[1], first_pair) = hasTwoPairs(conds[1], first_pair, p, i)
        if all(conds): return True
    return False
    
def incrementPassword(s: list[str]) -> list[str]:
    i = len(s) - 1
    while i >= 0 and s[i] == 'z':
        s[i] = 'a'
        i -= 1
    s[i] = chr(ord(s[i]) + 1)
    if s[i] == 'i' or s[i] == 'o' or s[i] == 'l':
        s[i] = chr(ord(s[i]) + 1)
    return s

def nextValidPassword(p: list[str]) -> list[str]:
    while not passwordIsValid(p):
        p = incrementPassword(p)
    return p

def solve(file):
    p = oldPassword(file)
    p1 = ''.join(nextValidPassword(p))
    p2 = ''.join(nextValidPassword(incrementPassword(p)))
    return p1 + '\n' + p2

start_time = time.time()
file = open(sys.argv[1], 'r')
print(solve(file))
file.close()
print("--- %s seconds ---" % (time.time() - start_time))