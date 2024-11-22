import sys
from collections import deque

with open(sys.argv[1]) as file:
    lines = file.read().strip()

grid = lines.split("\n")

pipe_map = {
    "|": [(1, 0), (-1, 0)],
    "-": [(0, 1), (0, -1)],
    "L": [(-1, 0), (0, 1)],
    "J": [(-1, 0), (0, -1)],
    "7": [(1, 0), (0, -1)],
    "F": [(1, 0), (0, 1)],
    ".": [],
}


def get_start_pipe_type(r, c):
    points = []
    for dr, dc in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
        for drr, dcc in pipe_map[grid[r + dr][c + dc]]:
            if dr + drr == 0 and dc + dcc == 0:
                points.append((dr, dc))
    assert len(points) == 2
    for pipe_type, moves in pipe_map.items():
        if all(point in moves for point in points):
            return pipe_type


def get_pipe_moves(r, c):
    pipe_type = grid[r][c] if grid[r][c] != "S" else get_start_pipe_type(r, c)
    return [(r + dr, c + dc) for dr, dc in pipe_map[pipe_type]]


# print(get_start_pipe_type(2, 0))

for r, row in enumerate(grid):
    for c, ch in enumerate(row):
        if ch == "S":
            sr = r
            sc = c
            break
    else:
        continue
    break


# BFS
visited = set()
queue = deque([(sr, sc)])

while queue:
    r, c = queue.popleft()
    if (r, c) in visited:
        continue
    visited.add((r, c))

    for rr, cc in get_pipe_moves(r, c):
        queue.append((rr, cc))

p1 = len(visited) // 2
p2 = 0
print(f"Part 1: {p1}")
print(f"Part 2: {p2}")
