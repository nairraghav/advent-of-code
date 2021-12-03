puzzle_input_list = []

with open("input.txt", "r") as puzzle_input:
    for line in puzzle_input:
        line = line.strip()
        puzzle_input_list.append(line)

index = 0
while len(puzzle_input_list) > 1:
    count_of_digits = {0: 0, 1: 0}

    for binary_string in puzzle_input_list:
        if binary_string[index] == "0":
            count_of_digits[0] += 1
        else:
            count_of_digits[1] += 1

    if count_of_digits[0] > count_of_digits[1]:
        digit_to_keep = "0"
    else:
        digit_to_keep = "1"

    puzzle_index = 0
    while puzzle_index < len(puzzle_input_list):
        if puzzle_input_list[puzzle_index][index] != digit_to_keep:
            del puzzle_input_list[puzzle_index]
        else:
            puzzle_index += 1
    index += 1

print(puzzle_input_list)

# quick and dirty was to copy code but change comparison logic for count of digits
puzzle_input_list = []

with open("input.txt", "r") as puzzle_input:
    for line in puzzle_input:
        line = line.strip()
        puzzle_input_list.append(line)

index = 0
while len(puzzle_input_list) > 1:
    count_of_digits = {0: 0, 1: 0}

    for binary_string in puzzle_input_list:
        if binary_string[index] == "0":
            count_of_digits[0] += 1
        else:
            count_of_digits[1] += 1

    if count_of_digits[0] <= count_of_digits[1]:
        digit_to_keep = "0"
    else:
        digit_to_keep = "1"

    puzzle_index = 0
    while puzzle_index < len(puzzle_input_list):
        if puzzle_input_list[puzzle_index][index] != digit_to_keep:
            del puzzle_input_list[puzzle_index]
        else:
            puzzle_index += 1
    index += 1

print(puzzle_input_list)

# used binary calculator to determine final answer
# 1800151