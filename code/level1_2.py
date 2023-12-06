filename = "inputs\level1_input.txt"

with open(filename) as file:
    lines = [line.rstrip() for line in file]

str_digits = {
    "one": 1,
    "two": 2,
    "three": 3,
    "four": 4,
    "five": 5,
    "six": 6,
    "seven": 7,
    "eight": 8,
    "nine": 9,
}
str_digits_rev = {
    "eno": 1,
    "owt": 2,
    "eerht": 3,
    "ruof": 4,
    "evif": 5,
    "xis": 6,
    "neves": 7,
    "thgie": 8,
    "enin": 9,
}


def calibrate(line):
    rev_line = line[::-1]
    last_digit = 99
    first_found = False
    last_found = False

    for i in range(len(line)):
        if line[i].isdigit():
            first_digit = line[i]
            break
        for j in range(3, 6):
            if line[i : i + j] in str_digits:
                first_digit = str(str_digits[line[i : i + j]])
                first_found = True
                break
        if first_found == True:
            break

    for i in range(0, len(rev_line)):
        if rev_line[i].isdigit():
            last_digit = rev_line[i]
            break
        for j in range(3, 6):
            if rev_line[i : i + j] in str_digits_rev:
                last_digit = str(str_digits_rev[rev_line[i : i + j]])
                last_found = True
                break
        if last_found == True:
            break

    if last_digit == 99:
        digits = "0"
    else:
        digits = first_digit + last_digit

    return int(digits)


total = 0

for line in lines:
    total += calibrate(line)

print(total)
