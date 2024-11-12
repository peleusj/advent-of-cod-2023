import sys

with open(sys.argv[1]) as file:
    lines = file.read().strip()

instructions, networks = lines.split("\n\n")


class LR:
    """Represent one node and its network"""

    def __init__(self, left, right):
        self.L = left
        self.R = right

    def __getitem__(self, direction):
        if direction == "L":
            return self.L
        else:
            return self.R


def parse():
    maps = {}
    for network in networks.split("\n"):
        node, neighbors = network.split(" = ")
        left, right = neighbors[1:-1].split(", ")
        lr = LR(left, right)
        maps[node] = lr
    return maps


maps = parse()

start = "AAA"
end = "ZZZ"
steps = 0
round = 1

while round > 0:
    for instruction in instructions:
        steps += 1
        next = maps[start][instruction]
        start = next
        if start == end:
            break
    if start == end:
        break

p1 = steps
p2 = 0


print(f"Part 1: {p1}")
print(f"Part 2: {p2}")
