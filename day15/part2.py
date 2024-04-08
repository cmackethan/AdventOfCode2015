import sys
import time
import itertools

class Ingredient:
    def __init__(self, line: str):
        line = line.strip().split()
        self.name = line[0].split(':')[0]
        self.capacity = line[2].split(',')[0]
        self.durability = line[4].split(',')[0]
        self.flavor = line[6].split(',')[0]
        self.texture = line[8].split(',')[0]
        self.calories = line[10]
    
    def toString(self) -> str:
        return 'name: ' + self.name + ', capacity: ' + self.capacity \
            + ', durability: ' + self.durability + ', flavor: ' + self.flavor \
            + ', texture: ' + self.texture + ', calories: ' + self.calories

class IngredientCalculator:
    def __init__(self, N: int, file):
        self.N = N
        self.ingredients: list[Ingredient] = [Ingredient(line) for line in file]

    def calculateScore(self, combination: tuple[int]) -> int:
        capacity: int = 0; durability: int = 0; flavor: int = 0; texture: int = 0; calories: int = 0
        for i, num in enumerate(combination):
            ingredient = self.ingredients[i]
            capacity += num * int(ingredient.capacity)
            durability += num * int(ingredient.durability)
            flavor += num * int(ingredient.flavor)
            texture += num * int(ingredient.texture)
            calories += num * int(ingredient.calories)
        if calories != 500:
            return 0
        return max(capacity, 0) * max(durability, 0) * max(flavor, 0) * max(texture, 0)
    
    def getHighScore(self) -> int:
        high_score: int = 0
        for combo in itertools.product(range(self.N + 1), repeat=len(self.ingredients)):
            if sum(combo) == 100:
                high_score = max(self.calculateScore(combo), high_score)
        return high_score

def solve(file):
    return IngredientCalculator(100, file).getHighScore()

start_time = time.time()
file = open(sys.argv[1], 'r')
print(solve(file))
file.close()
print("--- %s seconds ---" % (time.time() - start_time))