from pprint import pprint
from copy import deepcopy

def get_lines_from_input_stripped():
    output = list()
    with open("input.txt", "r") as puzzle_input:
        lines = puzzle_input.readlines()
        for line in lines:
            line = line.strip()
            if line:
                output.append([l for l in line])
    return output


def get_next_spot_character(position, mapped_area):
    current_row, current_col = position
    current_direction = mapped_area[current_row][current_col]
    try:
        match current_direction:
            case "^":
                return mapped_area[current_row - 1][current_col], current_row - 1, current_col
            case ">":
                return mapped_area[current_row][current_col + 1], current_row, current_col + 1
            case "v":
                return mapped_area[current_row + 1][current_col], current_row + 1, current_col
            case "<":
                return mapped_area[current_row][current_col - 1], current_row, current_col - 1
            case _:
                return None, None, None
    except Exception as e:
        print(e)
        return None, None, None


def is_mapped_area_cyclic(starting_position, mapped_area):
    unique_spots_visited = set()
    current_row, current_col = starting_position
    current_direction = mapped_area[current_row][current_col]
    unique_spots_visited.add((starting_position, current_direction))
    next_spot_character, next_row, next_col = get_next_spot_character(starting_position, mapped_area)
    while (next_spot_character is not None):
        if (next_row < 0) or (next_col < 0):
            break
        
        current_direction = mapped_area[current_row][current_col]
        if next_spot_character == ".":
            starting_position = (next_row, next_col)
            mapped_area[current_row][current_col] = "."
            mapped_area[next_row][next_col] = current_direction
            current_row, current_col = next_row, next_col

        if next_spot_character == "#":
            match current_direction:
                case "^":
                    mapped_area[current_row][current_col] = ">"
                case ">":
                    mapped_area[current_row][current_col] = "v"
                case "v":
                    mapped_area[current_row][current_col] = "<"
                case "<":
                    mapped_area[current_row][current_col] = "^"
                case _:
                    raise Exception
        
        next_spot_character, next_row, next_col = get_next_spot_character(starting_position, mapped_area)
        if (starting_position, mapped_area[current_row][current_col]) in unique_spots_visited:
            return True
        unique_spots_visited.add((starting_position, current_direction))
    return False


def main():
    running_sum = 0
    output = get_lines_from_input_stripped()
    #pprint(output)

    possible_positions = ("^", ">", "v", "<")
    for row in range(len(output)):
        for col in range(len(output[row])):
            if output[row][col] in possible_positions:
                starting_position = (row, col)

    for row in range(len(output)):
        for col in range(len(output[row])):
            print(row, col)
            if (row, col) != starting_position:
                output_clone = deepcopy(output)
                output_clone[row][col] = "#"
                #pprint(output_clone)
                if is_mapped_area_cyclic(starting_position, output_clone):
                    running_sum += 1

    #pprint(output)
    #print(unique_spots_visited)
    #print(len(unique_spots_visited))
    print(running_sum)

if __name__ == "__main__":
    main()
