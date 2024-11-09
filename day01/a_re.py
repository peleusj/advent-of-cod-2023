import sys
import re

with open(sys.argv[1]) as file:
    lines = file.readlines()


p1 = 0
p2 = 0

n = "one two three four five six seven eight nine".split()

# be careful with special case like 'sixeightwo'
# which last number should be two
pattern = "(?=(" + "|".join(n) + "|\\d))"


def trans(c):
    if c in n:
        return str(n.index(c) + 1)
    return c


for line in lines:
    p1_digits = [character for character in line if character.isdigit()]
    # p1_digits = list(filter(str.isdigit, line))
    # p1_digits = re.sub(r"\D", "", line)

    # re.sub can not use together with (?=...) lookahead assertion
    # p2_digits = re.findall(pattern, line)
    p2_digits = [*map(trans, re.findall(pattern, line))]
    # print(p2_digits)

    if p1_digits:
        p1 += int(p1_digits[0] + p1_digits[-1])

    if p2_digits:
        p2 += int(p2_digits[0] + p2_digits[-1])

print(f"Part 1: {p1}")
print(f"Part 2: {p2}")
