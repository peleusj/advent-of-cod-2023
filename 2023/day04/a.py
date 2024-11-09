import math
import sys

with open(sys.argv[1]) as file:
    lines = file.read().splitlines()

p1 = 0
p2 = 0

p2_cards = [1 for _ in range(len(lines))]


def parse(line):
    win_numbers, numbers = line.split(":")[1].split("|")
    count = 0
    for number in numbers.strip().split():
        if number in win_numbers.strip().split():
            count += 1
    return count


for index, line in enumerate(lines):
    count = parse(line)
    if count:
        p1 += int(math.pow(2, count - 1))

        for x in range(p2_cards[index]):
            for y in range(index + 1, index + 1 + count):
                p2_cards[y] += 1

p2 = sum(p2_cards)

print(f"Part 1: {p1}")
print(f"Part 2: {p2}")
