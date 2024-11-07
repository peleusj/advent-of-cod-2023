import sys
import math

with open(sys.argv[1]) as file:
    lines = file.readlines()

p1 = 0
p2 = 0

p1_bag = {"red": 12, "green": 13, "blue": 14}


def parse(line):
    """
    input:
        "Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green"
    output:
        [{'blue': 3, 'red': 4}, {'red': 1, 'green': 2, 'blue': 6}, {'green': 2}]
    """
    result = []
    for round in line.split(":")[1].split(";"):
        cubes = {}
        for pair in round.split(","):
            quantity, color = pair.split()
            cubes[color] = int(quantity)
        result.append(cubes)
    return result


t_lines = [parse(line) for line in lines]

for index, line in enumerate(t_lines):
    possibility = True
    p2_bag = {"red": 0, "green": 0, "blue": 0}
    for round in line:
        for color, quantity in round.items():
            if quantity > p1_bag[color]:
                possibility = False
            if quantity > p2_bag[color]:
                p2_bag[color] = quantity
    if possibility:
        p1 += index + 1

    p2 += math.prod(p2_bag.values())

print(f"Part 1: {p1}")
print(f"Part 2: {p2}")
