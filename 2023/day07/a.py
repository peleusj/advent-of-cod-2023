import sys
from collections import Counter

with open(sys.argv[1]) as file:
    lines = file.read().strip()

lines = lines.split("\n")

pairs = {line.split()[0]: int(line.split()[1]) for line in lines}
# print(pairs)

cards1 = "A, K, Q, J, T, 9, 8, 7, 6, 5, 4, 3, 2".split(", ")
cards2 = "A, K, Q, T, 9, 8, 7, 6, 5, 4, 3, 2, J".split(", ")
# print(cards)


def strength(hand, cards):
    return [cards.index(card) for card in hand]


def type_value(counter):
    values = list(counter.values())
    c = Counter(values)
    # Five of a kind
    if c.get(5, 0) == 1:
        return 1
    # Four of a kind
    elif c.get(4, 0) == 1:
        return 2
    # Full house
    elif c.get(3, 0) == 1 and c.get(2, 0) == 1:
        return 3
    # Three of a kind
    elif c.get(3, 0) == 1:
        return 4
    # Two pair
    elif c.get(2, 0) == 2:
        return 5
    # One pair
    elif c.get(2, 0) == 1:
        return 6
    # High card
    else:
        return 7


def hand_type(hand):
    counter = Counter(hand)
    return type_value(counter)


def hand_type_joker(hand):
    counter = Counter(hand)
    # print("=" * 8)
    # print(counter)
    joker_counts = 0
    if "J" in counter:
        joker_counts = counter["J"]
        if joker_counts == 5:
            counter = {"A": 5}
        else:
            del counter["J"]
            most_cards = max(counter, key=counter.get)
            counter[most_cards] += joker_counts
    # print(counter)
    return type_value(counter)


# hand_type_joker("23JJ4")
# hand_type_joker("233J4")
# hand_type_joker("JJJJJ")


p1_pairs = sorted(
    pairs.items(),
    key=lambda item: (hand_type(item[0]), strength(item[0], cards1)),
    reverse=True,
)

p2_pairs = sorted(
    pairs.items(),
    key=lambda item: (hand_type_joker(item[0]), strength(item[0], cards2)),
    reverse=True,
)


p1 = 0
p2 = 0

for i, (hand, score) in enumerate(p1_pairs):
    p1 += score * (i + 1)

for i, (hand, score) in enumerate(p2_pairs):
    p2 += score * (i + 1)

print(f"Part 1: {p1}")
print(f"Part 2: {p2}")
