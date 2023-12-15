filename = "inputs\level15_input.txt"

hash_input = ""

with open(filename) as file:
    lines = [line.rstrip() for line in file]
    for line in lines:
        hash_input += line

hash_list = hash_input.split(",")


def hash_algo(string):
    current_value = 0
    for char in string:
        current_value += ord(char)
        current_value *= 17
        current_value = current_value % 256

    return current_value


total = 0

for hash_string in hash_list:
    total += hash_algo(hash_string)

print(total)
