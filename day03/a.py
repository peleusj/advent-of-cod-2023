import sys
import string
import re

with open(sys.argv[1]) as file:
    lines = file.read().strip().split("\n")

p1 = 0
p2 = 0

punctuations = string.punctuation.replace(".", "")
pattern = r"\d+"
lens = len(lines)

for index, line in enumerate(lines):
    line_pre = lines[index - 1] if index > 0 else None
    line_after = lines[index + 1] if index < lens - 1 else None

    matches = re.finditer(pattern, line)

    for match in matches:
        start = int(match.start())
        end = int(match.end())

        if start > 0:
            if line[start - 1] in punctuations:
                p1 += int(match.group())
                continue

        if end < lens:
            if line[end] in punctuations:
                p1 += int(match.group())
                continue

        b_start = start - 1 if start > 0 else start
        b_end = end + 1 if end < lens else end

        if line_pre:
            for c in line_pre[b_start:b_end]:
                if c in punctuations:
                    p1 += int(match.group())
                    continue

        if line_after:
            for c in line_after[b_start:b_end]:
                if c in punctuations:
                    p1 += int(match.group())

print(f"Part 1: {p1}")
print(f"Part 2: {p2}")
