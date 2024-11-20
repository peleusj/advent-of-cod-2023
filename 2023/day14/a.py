import sys

with open(sys.argv[1]) as file:
    lines = file.read().strip()

grid = lines.split("\n")
columns = list(zip(*grid))


def slide_north(rocks):
    length = len(rocks)
    for i in range(length):
        if rocks[i] == "O":
            j = i
            while j > 0:
                if rocks[j - 1] == ".":
                    j -= 1
                else:
                    break
            if rocks[j] == ".":
                rocks[j], rocks[i] = rocks[i], rocks[j]
    return rocks


def calculate_load(rocks):
    total = 0
    length = len(rocks)
    for index, rock in enumerate(rocks):
        if rock == "O":
            total += length - index
    return total


# print(calculate_load(["O", "O", "O", "O", ".", ".", ".", ".", "#", "#"]))

columns = [slide_north(list(col)) for col in columns]
p1 = sum(calculate_load(col) for col in columns)

p2 = 0
print(f"Part 1: {p1}")
print(f"Part 2: {p2}")
