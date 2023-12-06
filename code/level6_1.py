from collections import defaultdict

filename = "inputs\level6_input.txt"

total = 1

with open(filename) as file:
    lines = [line.rstrip() for line in file]
    times = [time for time in lines[0].split(":")[1:][0].split(" ") if time != ""]
    distances = [dist for dist in lines[1].split(":")[1:][0].split("  ") if dist != ""]
    race_num = len(times)

for race in range(0, race_num):
    ways = 0
    race_time = int(times[race])
    record = int(distances[race])

    for hold_time in range(1, race_time):
        travel_time = race_time - hold_time
        distance = travel_time * hold_time

        if distance > record:
            ways += 1

    total *= ways

print(total)
