import sys
import time

class Present:
    def __init__(self, dimensions: list[str]):
        self.l = int(dimensions[0])
        self.w = int(dimensions[1])
        self.h = int(dimensions[2])

    def surfaceArea(self) -> int:
        return 2 * self.l * self.w + 2 * self.w * self.h + 2 * self.h * self.l
    
    def areaOfSmallestSide(self) -> int:
        return min([self.l * self.w, self.w * self.h, self.h * self.l])
    
    def paperRequired(self) -> int:
        return self.surfaceArea() + self.areaOfSmallestSide()

def solve(file) -> int:
    total_paper_required = 0
    for line in open(file, 'r'):
        present = Present(line.strip().split('x'))
        total_paper_required += present.paperRequired()
    return total_paper_required

start_time = time.time()
print(solve(sys.argv[1]))
print("--- %s seconds ---" % (time.time() - start_time))