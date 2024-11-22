import sys
from functools import lru_cache

with open(sys.argv[1]) as file:
    lines = file.read().strip()

lines = lines.split("\n")


@lru_cache
def get_combinations(springs, nums):
    if len(springs) == 0:
        return 1 if len(nums) == 0 else 0

    if len(nums) == 0:
        return 0 if "#" in springs else 1

    result = 0

    if springs[0] in ".?":
        result += get_combinations(springs[1:], nums)

    if springs[0] in "#?":
        n = nums[0]
        if (
            len(springs) >= n
            and "." not in springs[:n]
            and (len(springs) == n or springs[n] != "#")
        ):
            result += get_combinations(springs[n + 1 :], nums[1:])

    return result


def sum_combinatios(lines, fold=1):
    total = 0
    for line in lines:
        springs, nums = line.split(" ")
        springs = "?".join([springs] * fold)
        nums = tuple(map(int, nums.split(","))) * fold
        total += get_combinations(springs, nums)
    return total


p1 = sum_combinatios(lines)
p2 = sum_combinatios(lines, fold=5)
print(f"Part 1: {p1}")
print(f"Part 2: {p2}")
