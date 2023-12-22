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

def get_next_coordinate(start_x, start_y, symbol_x, symbol_y, symbol):
    match symbol:
        case "|":
            if symbol_y > start_y:
                return start_x, start_y + 2
            else:
                return start_x, start_y - 2
        case "-":
            if symbol_x > start_x:
                return start_x + 2, start_y
            else:
                return start_x - 2, start_y
        case "L":
            if symbol_y > start_y:
                return start_x + 1, start_y + 1
            else:
                return start_x - 1, start_y - 1
        case "J":
            if symbol_y > start_y:
                return start_x - 1, start_y + 1
            else:
                return start_x + 1, start_y - 1
        case "7":
            if symbol_y == start_y:
                return start_x + 1, start_y + 1
            else:
                return start_x - 1, start_y - 1
        case "F":
            if symbol_y < start_y:
                return start_x + 1, start_y - 1
            else:
                return start_x - 1, start_y + 1
        case ".":
            pass

def get_travel_path(lines, start_x, start_y):
    print(start_x, start_y, "\n")
    valid_paths = list()
    if lines[start_y][start_x + 1] in ("-", "J", "7"):
        valid_paths.append((start_x + 1, start_y))

    if lines[start_y][start_x - 1] in ("-", "L", "F"):
        valid_paths.append((start_x - 1, start_y))

    if lines[start_y-1][start_x] in ("|", "7", "F"):
        valid_paths.append((start_x, start_y - 1))

    if lines[start_y+1][start_x] in ("|", "L", "J"):
        valid_paths.append((start_x, start_y + 1))
    
    assert len(valid_paths) == 2
    path_one, path_two = valid_paths
    
    steps = 1
    old_one_x = start_x
    old_one_y = start_y
    old_two_x = start_x
    old_two_y = start_y
    while path_one != path_two:
        print(path_one, lines[path_one[1]][path_one[0]])
        print(path_two, lines[path_two[1]][path_two[0]])
        print("\n")
        temp_one_x, temp_one_y = path_one
        temp_two_x, temp_two_y = path_two
        path_one = get_next_coordinate(old_one_x, old_one_y, path_one[0], path_one[1], lines[path_one[1]][path_one[0]])
        path_two = get_next_coordinate(old_two_x, old_two_y, path_two[0], path_two[1], lines[path_two[1]][path_two[0]])
        old_one_x, old_one_y = temp_one_x, temp_one_y
        old_two_x, old_two_y = temp_two_x, temp_two_y
        steps += 1

    return steps


def main():
    lines = get_input()
    start_x, start_y = find_starting_point(lines)
    print(get_travel_path(lines, start_x, start_y))


if __name__ == "__main__":
    main()