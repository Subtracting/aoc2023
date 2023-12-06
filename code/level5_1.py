from collections import defaultdict

filename = "inputs\level5_input.txt"

mapping_dict = defaultdict(lambda: defaultdict(list))
min_location = 10**12

with open(filename) as file:
    lines = [line.rstrip() for line in file]
    source = ""
    destination = ""
    for line in lines:
        if "seeds" in line:
            seed_nums = list(map(int, line.split(" ")[1:]))
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


def map_to_range(source, source_type):
    ranges = mapping_dict[source_type]["ranges"]
    i = 0
    for rng in ranges:
        if source in rng:
            diff = mapping_dict[source_type]["diff"][i]
            destination = source + diff
            break
        else:
            destination = source
        i += 1

    return destination


for seed in mapping_dict["seeds"]:
    soil = map_to_range(seed, "seed")
    fertilizer = map_to_range(soil, "soil")
    water = map_to_range(fertilizer, "fertilizer")
    light = map_to_range(water, "water")
    temperature = map_to_range(light, "light")
    humidity = map_to_range(temperature, "temperature")
    location = map_to_range(humidity, "humidity")

    if location < min_location:
        min_location = location

print(min_location)
