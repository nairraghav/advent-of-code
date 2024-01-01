def get_input():
    puzzle_lines = list()
    with open("input.txt", "r") as puzzle_input:
        lines = puzzle_input.readlines()
        for line in lines:
            line = line.strip()
            line = [character for character in line]
            puzzle_lines.append(line)
    
    return puzzle_lines


def rotate_lines(lines):
    rotated_lines = list()
    for row_index in range(len(lines)):
        a = ""
        for column_index in range(len(lines[row_index])):
            a += lines[column_index][row_index]
        rotated_lines.append([character for character in a])

    return rotated_lines


def row_shift_zeroes_left(line):
    last_to_check = 0
    for index in range(len(line)):
        if line[index] == "O":
            check_index = index - 1
            possible_place_index = index

            while check_index >= last_to_check:
                if line[check_index] in ("O", "#"):
                    break
                else:
                    possible_place_index = check_index
                check_index -= 1

            if possible_place_index != index:
                line[possible_place_index], line[index] = line[index], line[possible_place_index]

    return line

    

def main():
    lines = get_input()
    rotated_lines = rotate_lines(lines)

    for row_index in range(len(rotated_lines)):
        rotated_lines[row_index] = row_shift_zeroes_left(rotated_lines[row_index])

    lines = rotate_lines(rotated_lines)
    
    total_load = 0
    counter = 1
    
    for line in lines[::-1]:
        number_of_rocks = len([rock for rock in line if rock == "O"]) * counter
        total_load += number_of_rocks
        counter += 1

    print(total_load)


if __name__ == "__main__":
    main()