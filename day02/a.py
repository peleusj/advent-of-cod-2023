import sys
from collections import defaultdict

with open(sys.argv[1]) as file:
    lines = file.read().splitlines()

p1 = 0
p2 = 0

p1_bag = {"red": 12, "green": 13, "blue": 14}


# Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green
for line in lines:
    p1_valid = True
    p2_bag = defaultdict(int)

    game, event = line.split(": ")

    for round in event.split("; "):
        for balls in round.split(", "):
            quantity, color = balls.split()
            if int(quantity) > p1_bag[color]:
                p1_valid = False
            p2_bag[color] = max(p2_bag[color], int(quantity))
    if p1_valid:
        p1 += int(game.split()[-1])

    base = 1
    for value in p2_bag.values():
        base *= value
    p2 += base

print(f"Part 1: {p1}")
print(f"Part 2: {p2}")
