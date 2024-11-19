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
                for j in range(1, max_steps + 1):
                    if pattern[p1 - j] != pattern[p2 + j]:
                        break
                else:
                    matches = p1 + 1

    return matches


def is_smudge(l1, l2):
    diff_cnt = 0
    for c1, c2 in zip(l1, l2):
        if c1 != c2:
            diff_cnt += 1
            if diff_cnt > 1:
                return False
    return diff_cnt == 1


def find_smudge(pattern):
    matches = []
    length = len(pattern)
    for i in range(length):
        for j in range(i + 1, length):
            if is_smudge(pattern[i], pattern[j]):
                matches.append((i, j))

    for i, j in matches:
        if (j - 1) // 2:
            continue
        else:
            pass


p1 = 0

for pattern in patterns:
    rows = pattern.split("\n")
    cols = list(zip(*rows))
    # p1 += find_reflection(rows) * 100 + find_reflection(cols)
    print(find_smudge(rows))
    print(find_smudge(cols))


p2 = 0
print(f"Part 1: {p1}")
print(f"Part 2: {p2}")
