import sys

with open(sys.argv[1]) as file:
    lines = file.read().strip()

patterns = lines.split("\n\n")


def find_reflection(pattern):
    matches = 0
    length = len(pattern)

    for i in range(length):
        if i + 1 < length:
            if pattern[i] == pattern[i + 1]:
                p1, p2 = i, i + 1
                max_steps = min(p1, length - p2 - 1)
                for n in range(1, max_steps + 1):
                    if pattern[p1 - n] != pattern[p2 + n]:
                        break
                else:
                    matches = p1 + 1

    return matches


p1 = 0

for pattern in patterns:
    rows = pattern.split("\n")
    cols = list(zip(*rows))
    p1 += find_reflection(rows) * 100 + find_reflection(cols)

p2 = 0
print(f"Part 1: {p1}")
print(f"Part 2: {p2}")
