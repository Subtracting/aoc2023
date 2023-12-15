filename = "inputs\level14_input.txt"


platforms = []

with open(filename) as file:
    lines = [line.rstrip() for line in file]
    platform = []
    for line in lines:
        platform.append(list(line))

total = 0

height, width = len(platform), len(platform[0])
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

for y in range(height):
    total += (height - y) * platform[y].count("O")

print(total)
