import sys
import time
import json

def getSum(obj):
    if type(obj) == int:
        return obj
    elif type(obj) == list:
        sum = 0
        for e in obj: sum += getSum(e)
        return sum
    elif type(obj) == dict:
        values = obj.values()
        if "red" in values:
            return 0
        else:
            return getSum(list(values))
    else:
        return 0

def solve(file):
    return getSum(json.load(file))

start_time = time.time()
file = open(sys.argv[1], 'r')
print(solve(file))
file.close()
print("--- %s seconds ---" % (time.time() - start_time))