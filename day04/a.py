import math
import sys

with open(sys.argv[1]) as file:
    lines = file.readlines()

p1 = 0
p2 = 0

cards = [1 for _ in range(len(lines))]


def check(line):
    win_numbers, numbers = line.split(":")[1].split("|")
    count = 0
    for number in numbers.strip().split():
        if number in win_numbers.strip().split():
            count += 1
    return count


for index, line in enumerate(lines):
    count = check(line)
    if count:
        p1 += int(math.pow(2, count - 1))
        for x in range(cards[index]):
            for y in range(index + 1, index + 1 + count):
                cards[y] += 1

p2 = sum(cards)

print(f"Part 1: {p1}")
print(f"Part 2: {p2}")
