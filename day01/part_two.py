import re

mappings = {
    "one": "1",
    "two": "2",
    "three": "3",
    "four": "4",
    "five": "5",
    "six": "6",
    "seven": "7",
    "eight": "8",
    "nine": "9",
}


def digit_sum(filename):
    result = []

    with open(filename) as file:
        for line in file:
            mapped = re.sub(
                "|".join(mappings.keys()),
                lambda match: mappings[match.group(0)],
                line,
            )
            digits = [character for character in mapped if character.isdigit()]
            if digits:
                digit_number = int(digits[0] + digits[-1])
                result.append(digit_number)

    return result
