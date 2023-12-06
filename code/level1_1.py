filename = "inputs\level1_input.txt"

with open(filename) as file:
    lines = [line.rstrip() for line in file]


def calibrate(line):
    digits = ""
    for char in line:
        if char.isdigit():
            first_digit = char
            break
    for char in line[::-1]:
        if char.isdigit():
            last_digit = char
            break
    digits = first_digit + last_digit

    return int(digits)


total = 0

for line in lines:
    total += calibrate(line)

print(total)
