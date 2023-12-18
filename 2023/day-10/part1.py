def get_input():
    puzzle_lines = list()
    with open("input.txt", "r") as puzzle_input:
        lines = puzzle_input.readlines()
        for line in lines:
            line = line.strip()
            line = [character for character in line]
            puzzle_lines.append(line)
    
    return puzzle_lines

def find_starting_point(lines):
    for y_index in range(len(lines)):
        for x_index in range(len(lines[y_index])):
            if lines[y_index][x_index] == "S":
                return (x_index, y_index)

    return (None, None)

def get_travel_path(lines, start_x, start_y):
    pass

def main():
    lines = get_input()
    start_x, start_y = find_starting_point(lines)
    path_traveled = get_travel_path(lines, start_x, start_y)


if __name__ == "__main__":
    main()