filename = "inputs\level8_input.txt"

route = dict()

with open(filename) as file:
    for line in file:
        if "RLLRR" in line:
            directions = list(line.rstrip())
        elif line != "":
            node = line.rstrip().split(" = ")
            vert_from = node[0]
            vert_to = node[1].replace("(", "").replace(")", "").split(", ")
            route[vert_from] = vert_to

steps = 0
vert_loc = "AAA"


while vert_loc != "ZZZ":
    for direction in directions:
        if direction == "L":
            vert_loc = route[vert_loc][0]
        else:
            vert_loc = route[vert_loc][1]

        steps += 1

print(steps)
