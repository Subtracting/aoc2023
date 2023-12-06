import csv
from collections import defaultdict


filename = "inputs\level2_input.csv"

game_dict = defaultdict(list)
win_state = {"red": 12, "green": 13, "blue": 14}

with open(filename, newline="") as csvfile:
    lines = csv.reader(csvfile, delimiter=";")

    for line in lines:
        game_list = line[0].split(":")
        game_id = int(game_list[0].split(" ")[1])
        grabs = []
        game_dict[game_id].append(game_list[1])
        for i in range(1, len(line)):
            game_dict[game_id].append(line[i])

total = 0

for game_id, grabs in game_dict.items():
    min_dict = {"red": 1, "green": 1, "blue": 1}
    power_set = 1
    for grab in grabs:
        picks = grab.split(", ")
        for pick in picks:
            val_col = pick.lstrip().split(" ")
            val = int(val_col[0])
            col = val_col[1]

            if val > min_dict[col]:
                min_dict[col] = val

    for k, v in min_dict.items():
        power_set *= v

    total += power_set

print(total)
