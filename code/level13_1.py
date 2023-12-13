filename = "inputs\level13_input.txt"


mirrors = []

with open(filename) as file:
    lines = [line.rstrip() for line in file]
    mirror = []
    for line in lines:
        line = str(line.replace(".", "0")).replace("#", "1")
        if line == "":
            mirrors.append(mirror)
            mirror = []
        else:
            mirror.append(list(map(int, line)))


def hor_reflection(mirror, height, width):
    for y in range(1, height):
        reflection = all(
            [
                mirror[y + y_offset][x] == mirror[y - y_offset - 1][x]
                for x in range(width)
                for y_offset in range(height)
                if y + y_offset < height and y - y_offset - 1 >= 0
            ]
        )

        if reflection:
            return y


def vert_reflection(mirror, height, width):
    for x in range(1, width):
        reflection = all(
            [
                mirror[y][x + x_offset] == mirror[y][x - x_offset - 1]
                for y in range(height)
                for x_offset in range(width)
                if x + x_offset < width and x - x_offset - 1 >= 0
            ]
        )

        if reflection:
            return x


hor_total = 0
vert_total = 0

for mirror in mirrors:
    height, width = len(mirror), len(mirror[0])
    hor_value = hor_reflection(mirror, height, width)
    vert_value = vert_reflection(mirror, height, width)
    if hor_value:
        hor_total += hor_value * 100
    if vert_value:
        vert_total += vert_value

total = hor_total + vert_total

print(total)
