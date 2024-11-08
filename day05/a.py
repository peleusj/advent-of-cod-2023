import sys

with open(sys.argv[1]) as file:
    lines = file.read().strip().split("\n\n")

lines = [line.split("\n") for line in lines]
# print(lines)
# [
#   ['seeds: 79 14 55 13'],
#   ['seed-to-soil map:', '50 98 2', '52 50 48'],
#   ['soil-to-fertilizer map:', '0 15 37', '37 52 2', '39 0 15'],
#   ['fertilizer-to-water map:', '49 53 8', '0 11 42', '42 0 7', '57 7 4'],
#   ['water-to-light map:', '88 18 7', '18 25 70'],
#   ['light-to-temperature map:', '45 77 23', '81 45 19', '68 64 13'],
#   ['temperature-to-humidity map:', '0 69 1', '1 0 69'],
#   ['humidity-to-location map:', '60 56 37', '56 93 4']
# ]


# ['79', '14', '55', '13']
seed_strs = lines[0][0].split(": ")[1].split()

seeds = [int(seed) for seed in seed_strs]


# print(parse(79, ["50 98 2", "52 50 48"]))
def parse(source, map_strs):
    result = source
    for str in map_strs:
        start_des, start_source, length = [int(x) for x in str.split()]
        if source < start_source:
            continue
        elif source > (start_source + length - 1):
            continue
        else:
            result = start_des + (source - start_source)

    return result


def parse_location(seed):
    target = seed
    for line in lines[1:]:
        target = parse(target, line[1:])
    return target


p1 = float("inf")
p2 = float("inf")

for seed in seeds:
    p1 = min(p1, parse_location(seed))

p2_seeds_start = seeds[::2]
p2_seeds_length = seeds[1::2]
for i in range(len(p2_seeds_length)):
    for seed in range(p2_seeds_start[i], p2_seeds_start[i] + p2_seeds_length[i]):
        p2 = min(p2, parse_location(seed))


print(f"Part 1: {p1}")
print(f"Part 2: {p2}")
