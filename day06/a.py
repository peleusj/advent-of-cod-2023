import math
import sys

with open(sys.argv[1]) as file:
    lines = file.read().strip()

lines = lines.split("\n")

times = lines[0].split()[1:]
distances = lines[1].split()[1:]
records = zip(times, distances)

p2_time = int("".join(times))
p2_distance = int("".join(distances))


def count_brutal(time_limit, record_distance):
    result = 0
    for t in range(time_limit + 1):
        if (time_limit - t) * t > record_distance:
            result += 1
    return result


def count_quadratic(t, d):
    """
    Time:      7  15   30
    Distance:  9  40  200
    (t - h) * h  - d > 0
    -h^2 + th - d > 0
    """
    a = -1
    b = t
    c = -d
    root1 = math.ceil((-b + pow(b * b - 4 * a * c, 0.5)) / (2 * a) + 0.0000001)
    root2 = math.floor((-b - pow(b * b - 4 * a * c, 0.5)) / (2 * a) - 0.0000001)

    return root2 - root1 + 1


p1 = 1
for time_limit, distance in records:
    p1 *= count_brutal(int(time_limit), int(distance))

# p2 = count_brutal(p2_time, p2_distance)
p2 = count_quadratic(p2_time, p2_distance)

print(f"Part 1: {p1}")
print(f"Part 2: {p2}")
