import sys
import time

def calculate(s: str) -> (int, int):
    im_line: int = len(s) - 2
    i: int = 0
    while i < len(s):
        if s[i] == '\\':
            if s[i + 1] == 'x': # Never OOB
                im_line -= 3
            else:
                im_line -= 1
            i += 1
        i += 1
    return (len(s), im_line)

def solve(file):
    cr_sum: int = 0; im_sum: int = 0
    for line in file:
        (cr_line, im_line) = calculate(line.strip())
        print('Code: ' + str(cr_line) + ' In-Memory: ' + str(im_line))
        cr_sum += cr_line; im_sum += im_line
        print(str(cr_sum) + ' - ' + str(im_sum))
    return cr_sum - im_sum

start_time = time.time()
file = open(sys.argv[1], 'r')
print(solve(file))
file.close()
print("--- %s seconds ---" % (time.time() - start_time))