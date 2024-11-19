import itertools
import sys
import re

with open(sys.argv[1]) as file:
    lines = file.read().strip()

records = lines.split("\n")


def get_damaged(spring):
    return [len(match) for match in re.findall(r"#+", spring)]


def get_combinations(position_nums, symbols=".#"):
    result = []
    for combination in itertools.product(symbols, repeat=position_nums):
        result.append("".join(combination))
    return result


def replace_unknown(original_spring, replacement):
    new_spring = original_spring
    for char in replacement:
        new_spring = new_spring.replace("?", char, 1)
    return new_spring


def get_possible_arrangements(record):
    arrangements = 0
    spring, damaged = record.split(" ")
    damaged = [int(item) for item in damaged.split(",")]
    unknown_nums = spring.count("?")
    all_combinations = get_combinations(unknown_nums)
    for combination in all_combinations:
        if get_damaged(replace_unknown(spring, combination)) == damaged:
            arrangements += 1
    return arrangements


p1 = 0

for record in records:
    p1 += get_possible_arrangements(record)


p2 = 0
print(f"Part 1: {p1}")
print(f"Part 2: {p2}")
