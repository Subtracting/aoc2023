from collections import defaultdict

filename = "inputs\level15_input.txt"

hash_input = ""

with open(filename) as file:
    lines = [line.rstrip() for line in file]
    for line in lines:
        hash_input += line

hash_list = hash_input.split(",")
hash_map = {k: {} for k in range(0, 256)}


def hash_algo(string):
    current_value = 0
    for char in string:
        current_value += ord(char)
        current_value *= 17
        current_value = current_value % 256

    return current_value


total = 0

for hash_string in hash_list:
    if "=" in hash_string:
        label, focal = hash_string.split("=")
        box_number = hash_algo(label)
        hash_map[box_number][label] = focal
    else:
        label = hash_string.split("-")[0]
        box_number = hash_algo(label)
        hash_map[box_number].pop(label, None)

for box_number, lenses in hash_map.items():
    i = 0
    for label, focal in lenses.items():
        i += 1
        total += (1 + box_number) * i * int(focal)

print(total)
