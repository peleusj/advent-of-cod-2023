def digit_sum(filename):
    result = []

    with open(filename) as file:
        for line in file:
            digits = [character for character in line if character.isdigit()]
            if digits:
                digit_number = int(digits[0] + digits[-1])
                result.append(digit_number)

    return sum(result)
