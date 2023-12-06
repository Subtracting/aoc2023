import csv
from collections import defaultdict
import math


filename = "inputs\level4_input.csv"

total = 0

with open(filename, newline="") as csvfile:
    cards = csv.reader(csvfile, delimiter=":")
    for card in cards:
        card_id = card[0].split(" ")[-1]
        numbers = card[1].lstrip().replace("  ", " ").split("|")
        winning = list(map(int, numbers[0].rstrip().split(" ")))
        have = list(map(int, numbers[1].lstrip().split(" ")))

        matches = 0

        for number in have:
            if number in winning:
                matches += 1

        score = math.floor(2 ** (matches - 1))
        total += score

print(total)
