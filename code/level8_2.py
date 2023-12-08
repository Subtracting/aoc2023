from operator import mul
from functools import reduce

filename = "inputs\level8_input.txt"

route = dict()

with open(filename) as file:
    for line in file:
        if "LRRLRLRLLRLRLRL" in line:
            directions = list(line.rstrip())
        elif line != "":
            node = line.rstrip().split(" = ")
            vert_from = node[0]
            vert_to = node[1].replace("(", "").replace(")", "").split(", ")
            route[vert_from] = vert_to

steps = 0
vert_locs = [node for node in route.keys() if node[-1] == "A"]
number_locs = len(vert_locs)

cycles = dict()
factors = set()

for vert_loc in vert_locs:
    orig_vert_loc = vert_loc
    steps = 0
    while vert_loc[-1] != "Z":
        for direction in directions:
            steps += 1
            if direction == "L":
                vert_loc = route[vert_loc][0]
            else:
                vert_loc = route[vert_loc][1]

    cycles[orig_vert_loc] = steps


print(cycles)


def prime_factors(n):
    i = 2
    while i * i <= n:
        if n % i:
            i += 1
        else:
            n //= i
            factors.add(i)
    if n > 1:
        factors.add(n)


for key, val in cycles.items():
    prime_factors(val)

print(reduce(mul, factors, 1))
