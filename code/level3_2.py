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

total = 0

for x in range(width):
    for y in range(height):
        if matrix[x][y] == "*":
            bottom_coords = [(x + 1, y), (x + 1, y + 1), (x + 1, y - 1)]
            top_coords = [(x - 1, y), (x - 1, y + 1), (x - 1, y - 1)]
            left_coords = [(x, y - 1)]
            right_coords = [(x, y + 1)]
            adjacent_coords = [bottom_coords, top_coords, left_coords, right_coords]

            directions = 0
            direction_coords = []
            factor = 1

            for coords in adjacent_coords:
                if coords == bottom_coords and not matrix[x + 1][y].isdigit():
                    if (
                        matrix[x + 1][y + 1].isdigit()
                        and matrix[x + 1][y - 1].isdigit()
                    ):
                        directions += 2
                        direction_coords.append((x + 1, y + 1))
                        direction_coords.append((x + 1, y - 1))
                        break
                elif coords == top_coords and not matrix[x - 1][y].isdigit():
                    if (
                        matrix[x - 1][y + 1].isdigit()
                        and matrix[x - 1][y - 1].isdigit()
                    ):
                        directions += 2
                        direction_coords.append((x - 1, y + 1))
                        direction_coords.append((x - 1, y - 1))
                        break
                for coord in coords:
                    adj_x, adj_y = coord
                    if 0 <= adj_x < width and 0 <= adj_y < height:
                        if matrix[adj_x][adj_y].isdigit():
                            directions += 1
                            direction_coords.append((adj_x, adj_y))
                            break

            if directions == 2:
                numbers = []
                for dir_coord in direction_coords:
                    dir_x, dir_y = dir_coord
                    number = [str(matrix[dir_x][dir_y])]
                    j = 1
                    right_flag = True
                    left_flag = True
                    for j in range(1, 3):
                        if matrix[dir_x][dir_y + j].isdigit() and right_flag == True:
                            number.append(str(matrix[dir_x][dir_y + j]))
                        else:
                            right_flag = False
                        if matrix[dir_x][dir_y - j].isdigit() and left_flag == True:
                            number.insert(0, str(matrix[dir_x][dir_y - j]))
                        else:
                            left_flag = False

                        if len(number) == 3:
                            break

                    number = int("".join(number))
                    factor *= number
                    numbers.append(number)

                total += factor

print(total)
