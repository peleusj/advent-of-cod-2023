import sys
from functools import reduce

with open(sys.argv[1]) as file:
    lines = file.read().strip()

lines = lines.split("\n")

p1 = 0
p2 = 0


def predict(nums):
    result = []
    nums = [nums[i + 1] - nums[i] for i in range(len(nums) - 1)]
    while any(x != 0 for x in nums):
        result.append(nums)
        nums = [nums[i + 1] - nums[i] for i in range(len(nums) - 1)]
    next = reduce(lambda x, y: x + y, [x[-1] for x in result])
    previous = reduce(lambda x, y: y - x, [x[0] for x in result][::-1])
    return (next, previous)


# print(predict([1, 3, 6, 10, 15, 21]))
# part 2 test answer is 2


for line in lines:
    line = [int(x) for x in line.split()]
    predict_forward = line[-1] + predict(line)[0]
    p1 += predict_forward
    predict_backward = line[0] - predict(line)[1]
    p2 += predict_backward

print(f"Part 1: {p1}")
print(f"Part 2: {p2}")
