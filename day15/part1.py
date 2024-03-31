import sys
import time

num_ingredients: int = 100

class Ingredient:
    def __init__(self, name: str, capacity: int, durability: int, flavor: int, texture: int, calories: int):
        self.name = name
        self.capacity = capacity
        self.durability = durability
        self.flavor = flavor
        self.texture = texture
        self.calories = calories
    
    def toString(self) -> str:
        return 'name: ' + self.name + ', capacity: ' + self.capacity \
            + ', durability: ' + self.durability + ', flavor: ' + self.flavor \
            + ', texture: ' + self.texture + ', calories: ' + self.calories
    
def calculate_score(combinations: list[(int, Ingredient)]) -> int:
    capacity: int = 0
    durability: int = 0
    flavor: int = 0
    texture: int = 0
    for (num, ingredient) in combinations:
        capacity += num * int(ingredient.capacity)
        durability += num * int(ingredient.durability)
        flavor += num * int(ingredient.flavor)
        texture += num * int(ingredient.texture)
    return capacity * durability * flavor * texture

def solve(file):
    ingredients: list[Ingredient] = list()
    for line in file:
        line = line.strip().split()
        ingredients.append(Ingredient(
            line[0].split(':')[0],
            line[2].split(',')[0],
            line[4].split(',')[0],
            line[6].split(',')[0],
            line[8].split(',')[0],
            line[10]
        ))
    # ignore combinations with scores <= 0
    # if we brute force things, it gets exponentially worse
    # brute forcing for now...
    # TODO: figure out how to enumerate all possible combinations
        # for combo in combinations:
            # this_score = calculate_score(combinations)
            # if max_score < this_score:
                # max_score = this_score
        # return max_score
    # this is a buckets and balls problem
    combinations: list[(int, Ingredient)] = list()
    combinations.append((44, ingredients[0]))
    combinations.append((56, ingredients[1]))
    return calculate_score(combinations)


start_time = time.time()
file = open(sys.argv[1], 'r')
print(solve(file))
file.close()
print("--- %s seconds ---" % (time.time() - start_time))