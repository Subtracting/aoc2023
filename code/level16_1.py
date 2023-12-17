import copy
import sys

sys.setrecursionlimit(1500)
filename = "inputs\level16_input.txt"

with open(filename) as file:
    lines = [line.rstrip() for line in file]
    grid = []
    for line in lines:
        grid.append([char for char in line.replace("\\", "7")])


def head_right(y, x, height, width, symbol):
    for k in range(x + 1, width):
        if grid[y][k] in ["."]:
            nrg_grid[y][k] = "#"
        else:
            direction = "left"
            next_move(y, k, height, width, direction)
            break


def head_left(y, x, height, width, symbol):
    for k in range(x - 1, -1, -1):
        if grid[y][k] in ["."]:
            nrg_grid[y][k] = "#"
        else:
            direction = "right"
            next_move(y, k, height, width, direction)
            break


def head_down(y, x, height, width, symbol):
    for k in range(y + 1, height):
        if grid[k][x] in ["."]:
            nrg_grid[k][x] = "#"
        else:
            direction = "top"
            next_move(k, x, height, width, direction)
            break


def head_up(y, x, height, width, symbol):
    for k in range(y - 1, -1, -1):
        if grid[k][x] in ["."]:
            nrg_grid[k][x] = "#"
        else:
            direction = "below"
            next_move(k, x, height, width, direction)
            break


def next_move(y, x, height, width, direction):
    if visited_directions[y][x][direction] == 0:
        visited_directions[y][x][direction] = 1
        if grid[y][x] == "7":  # \
            reflector_1(y, x, height, width, direction)
        elif grid[y][x] == "/":
            reflector_2(y, x, height, width, direction)
        elif grid[y][x] == "-":
            hor_splitter(y, x, height, width)
        elif grid[y][x] == "|":
            vert_splitter(y, x, height, width)


# \
def reflector_1(y, x, height, width, direction):
    nrg_grid[y][x] = "#"
    symbol = "7"

    # from top or right or below op left
    if direction == "top":
        head_right(y, x, height, width, symbol)
    elif direction == "right":
        head_up(y, x, height, width, symbol)
    elif direction == "below":
        head_left(y, x, height, width, symbol)
    elif direction == "left":
        head_down(y, x, height, width, symbol)


# /
def reflector_2(y, x, height, width, direction):
    nrg_grid[y][x] = "#"
    symbol = "/"

    # from top or right or below op left
    if direction == "top":
        head_left(y, x, height, width, symbol)
    elif direction == "right":
        head_down(y, x, height, width, symbol)
    elif direction == "below":
        head_right(y, x, height, width, symbol)
    elif direction == "left":
        head_up(y, x, height, width, symbol)


# -
def hor_splitter(y, x, height, width):
    nrg_grid[y][x] = "#"
    symbol = "-"

    # right fill
    head_right(y, x, height, width, symbol)

    # left fill
    head_left(y, x, height, width, symbol)


# |
def vert_splitter(y, x, height, width):
    nrg_grid[y][x] = "#"
    symbol = "|"

    # bottom fill
    head_down(y, x, height, width, symbol)

    # top fill
    head_up(y, x, height, width, symbol)


height, width = len(grid), len(grid[0])
nrg_grid = copy.deepcopy(grid)

# [left, right, top, below]
visited_directions = [
    [{"left": 0, "right": 0, "top": 0, "below": 0} for _ in range(width)]
    for _ in range(height)
]

start_y, start_x = (0, 0)
next_move(start_y, start_x, height, width, "left")

total = 0

for y in range(height):
    total += nrg_grid[y].count("#")


print(total)
