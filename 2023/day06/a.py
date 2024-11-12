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
    start = 0
    end = 0

    t1 = 0
    while t1 <= time_limit:
        if (time_limit - t1) * t1 > record_distance:
            start = t1
            break
        t1 += 1

    t2 = time_limit
    while t2 >= 0:
        if (time_limit - t2) * t2 > record_distance:
            end = t2
            break
        t2 -= 1

    return end - start + 1


p1 = 1
for time_limit, distance in records:
    p1 *= race(int(time_limit), int(distance))

p2 = race(p2_time, p2_distance)

print(f"Part 1: {p1}")
print(f"Part 2: {p2}")
