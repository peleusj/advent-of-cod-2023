import sys

with open(sys.argv[1]) as file:
    lines = file.read().strip()

p1_seeds, *blocks = lines.split("\n\n")
# print(seeds)
# print(blocks)

seeds = [int(seed) for seed in p1_seeds.split(":")[1].split()]
# print(seeds)
# [79, 14, 55, 13]

p1_seeds = seeds

p2_seeds = []
for i in range(0, len(seeds), 2):
    p2_seeds.append((seeds[i], seeds[i] + seeds[i + 1]))

# print(p2_seeds)
# [(79, 93), (55, 68)]


def parse(input, maps):
    output = input
    for map in maps:
        des, src, length = [int(x) for x in map.split()]
        if src <= input < src + length:
            output = (input - src) + des
    return output


# print(parse(79, [[50, 98, 2], [52, 50, 48]]))


def parse_range(input, maps):
    """
    input: list of (start, input_end) tuple
            # inclusive on the left, exclusive on the right
            # e.g. [1,3) = [1,2]
    """
    output = []
    for map in maps:
        des_start, src_start, length = [int(x) for x in map.split()]
        src_end = src_start + length
        out_ranged = []
        # (src_start, src_end) might cut (start,end)
        # [start                                       end]
        #          [src_start       src_end]
        # [BEFORE ][INTER                  ][AFTER        ]
        while input:
            (start, end) = input.pop()

            before = (start, min(end, src_start))
            if before[1] > before[0]:
                out_ranged.append(before)

            inter = (max(start, src_start), min(src_end, end))
            if inter[1] > inter[0]:
                output.append(
                    (inter[0] - src_start + des_start, inter[1] - src_start + des_start)
                )

            after = (max(src_end, start), end)
            if after[1] > after[0]:
                out_ranged.append(after)
        input = out_ranged
    return output + input


p1 = float("inf")
p2 = float("inf")

for seed in p1_seeds:
    target = seed
    for block in blocks:
        # ["50 98 2", "52 50 48"]
        maps = block.split("\n")[1:]
        target = parse(target, maps)
    p1 = min(p1, target)

p2_locations = []
for seed in p2_seeds:
    target = [seed]
    for block in blocks:
        maps = block.split("\n")[1:]
        target = parse_range(target, maps)
    p2_locations.append(min(target)[0])

p2 = min(p2_locations)


print(f"Part 1: {p1}")
print(f"Part 2: {p2}")
