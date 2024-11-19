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
        # for i in range(1, p1 + 1):
        #     if p2 + i < len(pattern):
        #         if pattern[p1 - i] == pattern[p2 + i]:
        #             continue
        #         else:
        #             return 0

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


# def mirror_check(pattern, p1, p2):
#     if (p2 - p1) % 2 == 0:
#         return 0
#     else:
#         if p1 > 0:
#             for i in range(1, p1 + 1):
#                 if p2 + i < len(pattern):
#                     if pattern[p1 - i] == pattern[p2 + i]:
#                         continue
#                     else:
#                         return 0
#         most_step = (p2 - p1) // 2
#         p = p1
#         if most_step:
#             for i in range(1, most_step + 1):
#                 if pattern[p1 + i] != pattern[p2 - i]:
#                     return 0
#                 else:
#                     p = p1 + i
#         return p + 1


def find_reflection_sumdge(pattern):
    length = len(pattern)
    result = 0
    smudges = []

    for start in range(length):
        for end in range(start + 1, length):
            if is_smudge(pattern[start], pattern[end]):
                smudges.append((start, end))

    for start, end in smudges:
        mirrored = mirror_check(pattern, start, end)
        if mirrored:
            result = mirrored
    return result


p1 = 0
p2 = 0

for pattern in patterns:
    rows = pattern.split("\n")
    cols = list(zip(*rows))
    p1 += find_reflection(rows) * 100 + find_reflection(cols)
    p2 += find_reflection_sumdge(rows) * 100 + find_reflection_sumdge(cols)
    # print(find_reflection_sumdge(rows))
    # print(find_smudge(cols))


print(f"Part 1: {p1}")
print(f"Part 2: {p2}")
