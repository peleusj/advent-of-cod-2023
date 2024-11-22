import sys

with open(sys.argv[1]) as file:
    lines = file.read().splitlines()

p1 = 0
p2 = 0

row_len = len(lines)
col_len = len(lines[0])

p1_cordinates = set()


def parse(r, c):
    s = ""
    while c < col_len and lines[r][c].isdigit():
        s += lines[r][c]
        c += 1
    return int(s)


# check 3x3 grid around the puncuation
# can also check grid around digits
for r, row in enumerate(lines):
    for c, char in enumerate(row):
        if char.isdigit() or char == ".":
            continue

        p2_cordinates = set()

        for cr in [r - 1, r, r + 1]:
            for cc in [c - 1, c, c + 1]:
                if cr < 0 or cr >= row_len or cc < 0 or cc >= col_len:
                    continue
                if lines[cr][cc].isdigit():
                    while cc > 0 and lines[cr][cc - 1].isdigit():
                        cc -= 1
                    p1_cordinates.add((cr, cc))
                    if char == "*":
                        p2_cordinates.add((cr, cc))

        if len(p2_cordinates) == 2:
            nums = [parse(r, c) for r, c in p2_cordinates]
            p2 += nums[0] * nums[1]

p1 = sum(parse(r, c) for r, c in p1_cordinates)

print(f"Part 1: {p1}")
print(f"Part 2: {p2}")
