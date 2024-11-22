import sys
import math
from functools import reduce

with open(sys.argv[1]) as file:
    lines = file.read().strip()

instructions, networks = lines.split("\n\n")


maps = {}
for network in networks.split("\n"):
    node, neighbors = network.split(" = ")
    left, right = neighbors[1:-1].split(", ")
    maps[node] = (left, right)


def reach():
    start, end = "AAA", "ZZZ"
    round, is_end = True, False
    steps = 0
    while round:
        for instruction in instructions:
            steps += 1
            if instruction == "L":
                next = maps[start][0]
            else:
                next = maps[start][1]
            if next == end:
                is_end = True
                break
            else:
                start = next
        if is_end:
            break
    return steps


def reach_z(start):
    round, is_end = True, False
    z_steps = []
    steps = 0
    while round:
        for instruction in instructions:
            steps += 1
            if instruction == "L":
                next = maps[start][0]
            else:
                next = maps[start][1]
            if next.endswith("Z"):
                z_steps.append(steps)
                is_end = True
                break
            else:
                start = next

        if is_end:
            break
    return steps


# print(reach_z("22A"))


def lcm(a, b):
    """Least Common Multiple"""
    return abs(a * b) // math.gcd(a, b)


def reach_simultaneously():
    starting_nodes = [node for node in maps.keys() if node.endswith("A")]
    z_steps = [reach_z(node) for node in starting_nodes]
    return reduce(lcm, z_steps)


p1 = reach()
p2 = reach_simultaneously()


print(f"Part 1: {p1}")
print(f"Part 2: {p2}")
