import sys


with open(sys.argv[1]) as file:
    lines = file.readlines()

p1 = 0
p2 = 0
n = "one two three four five six seven eight nine".split()

for line in lines:
    p1_digits = []
    p2_digits = []

    for i, c in enumerate(line):
        if c.isdigit():
            p1_digits.append(c)
            p2_digits.append(c)

        for index, num in enumerate(n):
            if line[i:].startswith(num):
                p2_digits.append(str(index + 1))

    if p1_digits:
        p1 += int(p1_digits[0] + p1_digits[-1])

    if p2_digits:
        p2 += int(p2_digits[0] + p2_digits[-1])


print(f"Part 1: {p1}")
print(f"Part 2: {p2}")
