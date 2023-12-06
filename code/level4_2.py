import csv
from collections import defaultdict

filename = "inputs\level4_input.csv"

card_dict = defaultdict(list)
total = 0

with open(filename, newline="") as csvfile:
    cards = csv.reader(csvfile, delimiter=":")
    for card in cards:
        card_id = int(card[0].split(" ")[-1])
        numbers = card[1].lstrip().replace("  ", " ").split("|")
        winning = list(map(int, numbers[0].rstrip().split(" ")))
        have = list(map(int, numbers[1].lstrip().split(" ")))

        score = 0

        for number in have:
            if number in winning:
                score += 1

        copies = list(range(card_id + 1, card_id + score + 1))

        card_dict[card_id] = copies

cards = []


def copy_recursion(card_id):
    if card_dict[card_id] == []:
        return True
    else:
        for copy in card_dict[card_id]:
            cards.append(copy)
            copy_recursion(copy)


for card_id in card_dict.keys():
    copy_recursion(card_id)

total = len(cards) + len(card_dict)

print(total)
