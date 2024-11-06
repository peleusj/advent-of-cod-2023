import sys
import math

with open(sys.argv[1]) as file:
    lines = file.readlines()

p1 = 0
p2 = 0

bag = {"red": 12, "green": 13, "blue": 14}


def trans(line):
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


t_lines = [trans(line) for line in lines]

for index, line in enumerate(t_lines):
    possibility = True
    least_quantity = {"red": 0, "green": 0, "blue": 0}
    for round in line:
        for color, quantity in round.items():
            if quantity > bag[color]:
                possibility = False
            if quantity > least_quantity[color]:
                least_quantity[color] = quantity
    if possibility:
        p1 += index + 1

    p2 += math.prod(least_quantity.values())

print(f"Part 1: {p1}")
print(f"Part 2: {p2}")
