import sys

with open(sys.argv[1]) as file:
    lines = file.read().strip()

patterns = lines.split("\n\n")


def mirror_check(pattern, p1, p2):
    if (p2 - p1) % 2 == 0:
        return 0

    # check outside
    if p1 > 0:
        max_steps = min(p1, len(pattern) - p2 - 1)
        for j in range(1, max_steps + 1):
            if pattern[p1 - j] != pattern[p2 + j]:
                return 0
            else:
                continue

    # no need to check inside
    if p2 - p1 == 1:
        return p1 + 1

    # check inside
    max_steps = (p2 - p1) // 2
    p = p1
    if max_steps:
        for j in range(1, max_steps + 1):
            if pattern[p1 + j] != pattern[p2 - j]:
                return 0
            else:
                p = p1 + j

    return p + 1


def p1_reflection(pattern):
    result = 0
    length = len(pattern)

    for i in range(length):
        if i + 1 < length:
            if pattern[i] == pattern[i + 1]:
                mirror = mirror_check(pattern, i, i + 1)
                if mirror:
                    result = mirror

    return result


def is_smudge(l1, l2):
    """check whether two lines only different in one symbol, aka smudge"""
    different_symbols = 0
    for c1, c2 in zip(l1, l2):
        if c1 != c2:
            different_symbols += 1
            if different_symbols > 1:
                return False
    return different_symbols == 1


def p2_reflection(pattern):
    # find qulified index pairs of smudge
    smudges = []
    length = len(pattern)
    for p1 in range(length):
        for p2 in range(p1 + 1, length):
            if is_smudge(pattern[p1], pattern[p2]):
                smudges.append((p1, p2))

    # check whether sumdges are possible mirrors
    result = 0
    for p1, p2 in smudges:
        mirror = mirror_check(pattern, p1, p2)
        if mirror:
            result = mirror
    return result


p1 = 0
p2 = 0

for pattern in patterns:
    rows = pattern.split("\n")
    cols = list(zip(*rows))
    p1 += p1_reflection(rows) * 100 + p1_reflection(cols)
    p2 += p2_reflection(rows) * 100 + p2_reflection(cols)


print(f"Part 1: {p1}")
print(f"Part 2: {p2}")
