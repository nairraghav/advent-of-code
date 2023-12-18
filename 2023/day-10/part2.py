def get_input():
    puzzle_lines = list()
    with open("input.txt", "r") as puzzle_input:
        lines = puzzle_input.readlines()
        for line in lines:
            line = line.strip()
            line = [int(item) for item in line.split()]
            line = line[-1::-1]
            print(line)
            puzzle_lines.append(line)
    
    return puzzle_lines

def check_last_line_for_zeroes(line):
    for digit in line:
        if digit != 0:
            return False

    return True

def get_next_digit(line):
    lines = [line]
    check_line = lines[-1]
    while not check_last_line_for_zeroes(check_line):
        new_line = list()
        for line_index in range(1, len(check_line)):
            new_line.append(check_line[line_index] - check_line[line_index - 1])

        lines.append(new_line)
        check_line = lines[-1]

    running_sum = 0
    for line in lines:
        running_sum += line[-1]
    return running_sum

def main():
    lines = get_input()
    running_sum = 0
    for line in lines:
        running_sum += get_next_digit(line)

    print(running_sum)


if __name__ == "__main__":
    main()