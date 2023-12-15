import math

filename = "inputs\level14_input.txt"
platforms = []

with open(filename) as file:
    lines = [line.rstrip() for line in file]
    platform = []
    for line in lines:
        platform.append(list(line))


def north(height, width, platform):
    global total
    for x in range(width):
        for y in range(1, height):
            if platform[y][x] == "O":
                j = 1
                while (y - j) >= 0:
                    if platform[y - j][x] in ["O", "#"]:
                        break
                    j += 1
                if j > 1:
                    platform[y - j + 1][x] = "O"
                    platform[y][x] = "."

    return platform


def south(height, width, platform):
    global total
    for x in range(width):
        for y in reversed(range(0, height - 1)):
            if platform[y][x] == "O":
                j = 1
                while (y + j) < height:
                    if platform[y + j][x] in ["O", "#"]:
                        break
                    j += 1
                if j > 1:
                    platform[y + j - 1][x] = "O"
                    platform[y][x] = "."

    return platform


def west(height, width, platform):
    global total
    for y in range(height):
        for x in range(1, width):
            if platform[y][x] == "O":
                j = 1
                while (x - j) >= 0:
                    if platform[y][x - j] in ["O", "#"]:
                        break
                    j += 1
                if j > 1:
                    platform[y][x - j + 1] = "O"
                    platform[y][x] = "."

    return platform


def east(height, width, platform):
    global total
    for y in range(height):
        for x in reversed(range(0, width - 1)):
            if platform[y][x] == "O":
                j = 1
                while (x + j) < width:
                    if platform[y][x + j] in ["O", "#"]:
                        break
                    j += 1
                if j > 1:
                    platform[y][x + j - 1] = "O"
                    platform[y][x] = "."

    return platform


def cycle(height, width, platform):
    platform = north(height, width, platform)
    platform = west(height, width, platform)
    platform = south(height, width, platform)
    platform = east(height, width, platform)

    return platform


cycle_count = 0
states = []
height, width = len(platform), len(platform[0])

sol = (((1000000000 - 115) / 34) - math.floor((1000000000 - 115) / 34)) * 34


while True:
    total = 0
    platform = cycle(height, width, platform)

    for y in range(height):
        total += (height - y) * platform[y].count("O")

    cycle_count += 1
    if cycle_count == (int(sol) + 116):
        print(total)
        break
