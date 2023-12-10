from matplotlib import pyplot as plt


filename = "inputs\level10_input.txt"

connected = {
    "|": [(1, 0), (-1, 0)],
    "-": [(0, 1), (0, -1)],
    "L": [(-1, 0), (0, 1)],
    "J": [(-1, 0), (0, -1)],
    "7": [(1, 0), (0, -1)],
    "F": [(1, 0), (0, 1)],
}

neighbours = {
    (-1, 0): ["|", "F", "7"],
    (1, 0): ["|", "L", "J"],
    (0, 1): ["-", "J", "7"],
    (0, -1): ["-", "F", "L"],
}

matrix = []

with open(filename) as file:
    lines = [line.rstrip() for line in file]
    width, height = len(lines[0]), len(lines)
    for line in lines:
        row = list(line)
        matrix.append(row)

connected_matrix = [[0 for _ in range(width)] for _ in range(height)]


def check_connected(y, x):
    value = matrix[y][x]

    if value not in [".", "S"]:
        connection = connected[value]
        for adjacent in connection:
            adj_y, adj_x = adjacent
            if 0 <= (y + adj_y) < height and 0 <= (x + adj_x) < width:
                if matrix[y + adj_y][x + adj_x] == "S":
                    return (start_y, start_x)
                if (
                    matrix[y + adj_y][x + adj_x] in neighbours[(adj_y, adj_x)]
                    and (y + adj_y, x + adj_x) not in seen
                ):
                    return (y + adj_y, x + adj_x)


def get_S(matrix):
    for y in range(height):
        for x in range(width):
            if matrix[y][x] == "S":
                return (y, x)


start_y, start_x = get_S(matrix)
current_y, current_x = start_y + 1, start_x

connected_matrix[start_y][start_x] = 0
connected_matrix[current_y][current_x] = 1

seen = [(start_y, start_x)]
step = 1

path_coords = []

while (current_y, current_x) not in seen:
    step += 1
    seen.append((current_y, current_x))
    current_y, current_x = check_connected(current_y, current_x)
    connected_matrix[current_y][current_x] = step
    path_coords.append([current_y, current_x])

left_coords = {
    (0, 1): (-1, 0),  # right
    (0, -1): (1, 0),  # left
    (1, 0): (0, 1),  # down
    (-1, 0): (0, -1),  # up
}


def mark_left(y, x):
    if 0 <= (y) < height and 0 <= (x) < width:
        if connected_matrix[y][x] == 0:
            connected_matrix[y][x] = -1


for coord in range(1, len(path_coords)):
    coord1_y, coord1_x = path_coords[coord]
    coord2_y, coord2_x = path_coords[coord - 1]
    direction = (coord1_y - coord2_y, coord1_x - coord2_x)
    left_direction_y, left_direction_x = left_coords[direction]
    left_tile_y, left_tile_x = (
        coord1_y + left_direction_y,
        coord1_x + left_direction_x,
    )

    mark_left(left_tile_y, left_tile_x)

    if matrix[coord1_y][coord1_x] == "J" and direction == (1, 0):
        left_tile_y, left_tile_x = (
            coord1_y + 1,
            coord1_x,
        )
        mark_left(left_tile_y, left_tile_x)

    elif matrix[coord1_y][coord1_x] == "F" and direction == (-1, 0):
        left_tile_y, left_tile_x = (
            coord1_y - 1,
            coord1_x,
        )
        mark_left(left_tile_y, left_tile_x)


tiles = 0

for y in range(height):
    for x in range(0, width):
        if connected_matrix[y][x] == -1:
            left = 1
            right = 1
            up = 1
            down = 1

            while connected_matrix[y][x - left] == 0:
                connected_matrix[y][x - left] = -1
                left += 1
            while connected_matrix[y][x + right] == 0:
                connected_matrix[y][x + right] = -1
                right += 1
            while connected_matrix[y - up][x] == 0:
                connected_matrix[y - up][x] = -1
                up += 1
            while connected_matrix[y + down][x] == 0:
                connected_matrix[y + down][x] = -1
                down += 1


total = sum([row.count(-1) for row in connected_matrix])
print(total)
