from collections import defaultdict, deque
import itertools


filename = "inputs\level11_input.txt"

matrix = []


with open(filename) as file:
    lines = [line.rstrip() for line in file]
    for line in lines:
        row = list(line)
        matrix.append(row)


width, height = len(matrix[0]), len(matrix)


def expand_matrix(matrix):
    for x in reversed(range(width)):
        if all([matrix[y][x] == "." for y in range(height)]):
            for y in range(height):
                matrix[y][x] = "e"

    new_width = len(matrix[0])
    for y in reversed(range(height)):
        if set(matrix[y]) == {".", "e"} or set(matrix[y]) == {"."}:
            matrix[y] = ["e" for _ in range(new_width)]

    return matrix


matrix = expand_matrix(matrix)
width, height = len(matrix[0]), len(matrix)
print("expanded", width, height)


def adjacent_paths(matrix, cell, n, m):
    y, x = cell
    cell_p = []

    # bottom neighbours
    if y + 1 < m:
        if matrix[y + 1][x] in [".", "#", "e"]:
            cell_p.append((y + 1, x))

    # top neighbours
    if y - 1 >= 0:
        if matrix[y - 1][x] in [".", "#", "e"]:
            cell_p.append((y - 1, x))

    # left neighbour
    if x - 1 >= 0:
        if matrix[y][x - 1] in [".", "#", "e"]:
            cell_p.append((y, x - 1))

    # right neighbour
    if x + 1 < n:
        if matrix[y][x + 1] in [".", "#", "e"]:
            cell_p.append((y, x + 1))

    return cell_p


def maze_BFS(matrix, root, goal):
    queue = deque()
    visited = set(root)
    parents = defaultdict(tuple)

    queue.append(root)

    while queue != deque():
        cell = queue.popleft()

        if cell == goal:
            return cell

        for edge in adjacent_paths(matrix, cell, width, height):
            if edge not in visited:
                visited.add(edge)
                parents[edge] = cell
                queue.append(edge)

    return parents


def shortest_path(matrix, pairs):
    total = 0
    goal = (height, width)

    expansion = 1000000

    i = 0
    for pair in pairs:
        i += 1
        start = pair[0]
        cell_path = pair[1]
        paths = maze_BFS(matrix, start, goal)
        print(i)

        while cell_path != start:
            path_y, path_x = cell_path
            if matrix[path_y][path_x] == "e":
                total += expansion
            else:
                total += 1
            cell_path = paths[cell_path]

    return total


galaxies = []
sorted_galaxies = []

for y in range(height):
    for x in range(width):
        if matrix[y][x] == "#":
            if sorted((x, y)) not in sorted_galaxies:
                sorted_galaxies.append(tuple(sorted((x, y))))
                galaxies.append((y, x))


pairs = itertools.combinations(galaxies, 2)

print(shortest_path(matrix, pairs))
