import sys
import time
import hashlib

def solve(file):
    secret = open(file, 'r').readlines()[0]
    i: int = 0
    while hashlib.md5(str(secret + str(i)).encode()).hexdigest()[0:6] != '000000':
        i += 1
    return i

start_time = time.time()
print(solve(sys.argv[1]))
print("--- %s seconds ---" % (time.time() - start_time))