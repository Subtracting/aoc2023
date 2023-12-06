from collections import defaultdict
import sys

filename = "inputs\level5_input.txt"

mapping_dict = defaultdict(lambda: defaultdict(list))

with open(filename) as file:
    lines = [line.rstrip() for line in file]
    source = ""
    destination = ""
    for line in lines:
        if "seeds" in line:
            seed_nums = list(map(int, line.split(" ")[1:]))
            seed_nums = [seed_nums[i : i + 2] for i in range(0, len(seed_nums) - 2, 2)]
            mapping_dict["seeds"] = seed_nums
        elif "map" in line:
            map_select = line.split(" ")[0].split("-")
            source = map_select[0]
            destination = map_select[2]
        elif len(line) > 1:
            values = line.split(" ")

            dest_start = int(values[0])
            source_start = int(values[1])
            length = int(values[2])
            diff = -(source_start - dest_start)

            mapping_dict[source]["ranges"].append(
                range(source_start, source_start + length)
            )
            mapping_dict[source]["diff"].append(diff)


def rev_map(destination, destination_type):
    diffs = mapping_dict[destination_type]["diff"]
    i = 0
    for diff in diffs:
        rng = mapping_dict[destination_type]["ranges"][i]
        if destination - diff in rng:
            source = destination - diff
            break
        else:
            source = destination
        i += 1
    return source


for location in range(0, 836040384):
    humidity = rev_map(location, "humidity")
    temperature = rev_map(humidity, "temperature")
    light = rev_map(temperature, "light")
    water = rev_map(light, "water")
    fertilizer = rev_map(water, "fertilizer")
    soil = rev_map(fertilizer, "soil")
    seed = rev_map(soil, "seed")

    for start_seed, seed_length in mapping_dict["seeds"]:
        if seed in range(start_seed, start_seed + seed_length):
            print(location)
            sys.exit()
