import sys
import time

def calculate(s: str) -> (int, int):
    im_line: int = len(s) + 2
    for c in s:
        if c == '\"' or c == '\\':
            im_line += 1
    return (len(s), im_line)

def solve(file):
    cr_sum: int = 0; im_sum: int = 0
    for line in file:
        (cr_line, im_line) = calculate(line.strip())
        print('Code: ' + str(cr_line) + ' In-Memory: ' + str(im_line))
        cr_sum += cr_line; im_sum += im_line
    print(str(im_sum) + ' - ' + str(cr_sum))
    return im_sum - cr_sum

start_time = time.time()
file = open(sys.argv[1], 'r')
print(solve(file))
file.close()
print("--- %s seconds ---" % (time.time() - start_time))