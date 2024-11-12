import sys

with open(sys.argv[1]) as file:
    lines = file.read().strip()

lines = lines.split("\n")

times = lines[0].split()[1:]
distances = lines[1].split()[1:]
records = zip(times, distances)

p2_time = int("".join(times))
p2_distance = int("".join(distances))


def race(time_limit, record_distance):
    result = 0
    for t in range(time_limit + 1):
        if (time_limit - t) * t > record_distance:
            result += 1
    return result


p1 = 1
for time_limit, distance in records:
    p1 *= race(int(time_limit), int(distance))

p2 = race(p2_time, p2_distance)

print(f"Part 1: {p1}")
print(f"Part 2: {p2}")
