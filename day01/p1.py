ans = 0

for line in open(0):
    digits = [character for character in line if character.isdigit()]
    ans += int(digits[0] + digits[-1])

print(ans)
