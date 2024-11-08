import sys
from collections import defaultdict

with open(sys.argv[1]) as file:
    lines = file.read().strip().split("\n\n")

p1 = 0
p2 = 0


# print(source_destination_map(["50 98 2", "52 50 48"]).get(79))
def source_destination_map(str_list):
    result = defaultdict(int)
    for str in str_list:
        d_start, s_start, length = str.split()
        d_list = [d for d in range(int(d_start), int(d_start) + int(length) + 1)]
        s_list = [s for s in range(int(s_start), int(s_start) + int(length) + 1)]
        for i in range(int(length)):
            result[s_list[i]] = d_list[i]
    return result


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

seeds = lines[0][0].split(": ")[1].split()

seeds_location = []
for seed in seeds:
    # don't forget int convert
    target = int(seed)
    for line in lines[1:]:
        mappings = source_destination_map(line[1:])
        target = mappings.get(target, target)
    seeds_location.append(target)

p1 = min(seeds_location)


print(f"Part 1: {p1}")
print(f"Part 2: {p2}")
