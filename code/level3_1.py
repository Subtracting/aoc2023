filename = "inputs\level3_input.txt"

matrix = []
symbols = set()

with open(filename) as file:
    lines = [line.rstrip() for line in file]

    for line in lines:
        row = ["."]
        for x in line:
            row.append(x)
            if x != "." and not x.isdigit():
                symbols.add(x)
        row.append(".")
        matrix.append(row)


height, width = 140, 140

seen = [[0 for _ in range(142)] for _ in range(142)]

for x in range(width):
    for y in range(height):
        if matrix[x][y].isdigit():
            adjacent_coords = [
                (x + 1, y),
                (x - 1, y),
                (x, y + 1),
                (x, y - 1),
                (x + 1, y + 1),
                (x - 1, y + 1),
                (x + 1, y - 1),
                (x - 1, y - 1),
            ]
            hor_coords = [(x, y + 1), (x, y - 1)]

            for coord in adjacent_coords:
                adj_x, adj_y = coord
                if 0 <= adj_x < width and 0 <= adj_y < height:
                    if matrix[adj_x][adj_y] in symbols:
                        seen[x][y] = 1

            for hor_coord in hor_coords:
                hor_x, hor_y = hor_coord
                if 0 <= hor_x < width and 0 <= hor_y < height:
                    if matrix[hor_x][hor_y].isdigit() and seen[x][y] == 1:
                        seen[hor_x][hor_y] = 1

total = 0

for x in range(width):
    for y in range(height):
        if seen[x][y] == 1 and seen[x][y + 1] == 0:
            number = [str(matrix[x][y])]
            j = 1
            while matrix[x][y - j].isdigit() and len(number) <= 3:
                number.insert(0, str(matrix[x][y - j]))
                if matrix[x][y + 1].isdigit():
                    number.append(str(matrix[x][y + 1]))
                j += 1

            number = "".join(number)
            total += int(number)

print(total)
