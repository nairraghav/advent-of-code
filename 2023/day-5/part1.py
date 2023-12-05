def get_lines_from_input_stripped():
    output_lines = list()
    with open("input.txt", "r") as puzzle_input:
        lines = puzzle_input.readlines()
        for line in lines:
            line = line.strip()
            if line:
                output_lines.append(line)
        
    return output_lines


def get_mapped_value(map, source):
    destination = None
    for source_start, destination_start, range_length in map:
        if source_start <= source <= source_start + range_length:
            difference = source - source_start
            return destination_start + difference
    return source 

def parse_input(lines):
    seeds = lines[0].split(":")[1].strip()
    seeds = seeds.split()
    seeds = [int(seed) for seed in seeds]
    seed_to_soil = list()
    soil_to_fertilizer = list()
    fertilizer_to_water = list()
    water_to_light = list()
    light_to_temperature = list()
    temperature_to_humidity = list()
    humidity_to_location = list()
    maps = (seed_to_soil, soil_to_fertilizer, fertilizer_to_water, water_to_light, light_to_temperature, temperature_to_humidity, humidity_to_location)
    map_count = -1
    for line in lines[1:]:
        if "map:" in line:
            map_count += 1
        else:
            destination_start, source_start, range_length = line.split()
            destination_start = int(destination_start)
            source_start = int(source_start)
            range_length = int(range_length)
            maps[map_count].append((source_start, destination_start, range_length))
    return seeds, maps

def main():
    lines = get_lines_from_input_stripped()
    seeds, maps = parse_input(lines)

    import math
    lowest_location = math.inf
    for seed in seeds:
        soil = get_mapped_value(maps[0], seed)
        fertilizer = get_mapped_value(maps[1], soil)
        water = get_mapped_value(maps[2], fertilizer)
        light = get_mapped_value(maps[3], water)
        temperature = get_mapped_value(maps[4], light)
        humidity = get_mapped_value(maps[5], temperature)
        location = get_mapped_value(maps[6], humidity)

        lowest_location = min(location, lowest_location)

    print(lowest_location)

if __name__ == "__main__":
    main()