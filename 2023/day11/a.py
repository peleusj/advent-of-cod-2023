import sys
from itertools import combinations

with open(sys.argv[1]) as file:
    lines = file.read().strip()

grid = lines.split("\n")

galaxies = [
    (r, c) for r, row in enumerate(grid) for c, col in enumerate(row) if col == "#"
]

empty_rows = [r for r, row in enumerate(grid) if all(c == "." for c in row)]
empty_cols = [c for c, col in enumerate(zip(*grid)) if all(r == "." for r in col)]


def manhattan_distance(g1, g2, expand=2):
    r1, c1 = g1
    r2, c2 = g2
    distance = 0
    for r in range(min(r1, r2), max(r1, r2)):
        distance += expand if r in empty_rows else 1
    for c in range(min(c1, c2), max(c1, c2)):
        distance += expand if c in empty_cols else 1
    return distance


p1 = 0
p2 = 0

for g1, g2 in combinations(galaxies, 2):
    p1 += manhattan_distance(g1, g2)
    p2 += manhattan_distance(g1, g2, expand=1000000)

print(f"Part 1: {p1}")
print(f"Part 2: {p2}")
