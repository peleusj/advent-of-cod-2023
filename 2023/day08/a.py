import sys

with open(sys.argv[1]) as file:
    lines = file.read().strip()

instructions, networks = lines.split("\n\n")


maps = {}
for network in networks.split("\n"):
    node, neighbors = network.split(" = ")
    left, right = neighbors[1:-1].split(", ")
    maps[node] = (left, right)


def reach():
    start = "AAA"
    end = "ZZZ"
    steps = 0
    round = 1
    while round > 0:
        for instruction in instructions:
            steps += 1
            if instruction == "L":
                next = maps[start][0]
            else:
                next = maps[start][1]
            start = next
            if start == end:
                break
        if start == end:
            break
    return steps


def reach_simultaneously():
    starting_nodes = [node for node in maps.keys() if node.endswith("A")]
    length = len(starting_nodes)
    z_nodes = []
    round = 0
    steps = 0
    while round >= 0:
        for instruction in instructions:
            steps += 1
            if instruction == "L":
                next_nodes = [maps[node][0] for node in starting_nodes]
            else:
                next_nodes = [maps[node][1] for node in starting_nodes]
            starting_nodes = next_nodes
            print(starting_nodes)
            z_nodes = [node for node in starting_nodes if node.endswith("Z")]
            if len(z_nodes) == length:
                break

        if len(z_nodes) == length:
            break

    return steps


p1 = reach()
p2 = reach_simultaneously()


print(f"Part 1: {p1}")
print(f"Part 2: {p2}")
