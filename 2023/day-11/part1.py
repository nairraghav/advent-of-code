def get_input():
    puzzle_lines = list()
    with open("input.txt", "r") as puzzle_input:
        lines = puzzle_input.readlines()
        for line in lines:
            line = line.strip()
            line = [character for character in line]
            puzzle_lines.append(line)
    
    return puzzle_lines

def is_row_empty(line):
    for character in line:
        if character != ".":
            return False
    return True

def expand_universe(lines):
    y_index = 0
    while y_index < len(lines):
        current_row = lines[y_index]
        if is_row_empty(current_row):
            new_row = [character for character in current_row]
            lines.insert(y_index, new_row)
            y_index += 2
        else:
            y_index += 1

    x_index = 0
    while x_index < len(lines[0]):
        current_column = [line[x_index] for line in lines]
        if is_row_empty(current_column):
            for line in lines:
                line.insert(x_index, ".")
            x_index += 2
        else:
            x_index += 1
    return lines


def get_all_galaxies(lines):
    galaxies = list()
    
    for y_index in range(len(lines)):
        for x_index in range(len(lines[y_index])):
            if lines[y_index][x_index] == "#":
                galaxies.append((x_index, y_index))

    return galaxies

def get_distance_between_galaxies(start_x, start_y, end_x, end_y):
    return abs(end_x - start_x) + abs(end_y - start_y)

def main():
    lines = get_input()
    lines = expand_universe(lines)
    
    galaxies = get_all_galaxies(lines)
    
    running_sum = 0
    for current_galaxy_index in range(len(galaxies) - 1):
        for comparing_galaxy_index in range(current_galaxy_index+1, len(galaxies)):
            current_galaxy_x, current_galaxy_y = galaxies[current_galaxy_index]
            comparing_galaxy_x, comparing_galaxy_y = galaxies[comparing_galaxy_index]
            running_sum += get_distance_between_galaxies(current_galaxy_x, current_galaxy_y, comparing_galaxy_x, comparing_galaxy_y)

    print(running_sum)


if __name__ == "__main__":
    main()