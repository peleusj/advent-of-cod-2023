import sys

with open(sys.argv[1]) as file:
    lines = file.read().split("\n\n")

p1 = 0
p2 = 0

print([line.split("\n") for line in lines])

print(f"Part 1: {p1}")
print(f"Part 2: {p2}")
