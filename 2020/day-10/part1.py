
with open("input.txt", "r") as puzzle_input:
    puzzle_input = [int(line.strip()) for line in puzzle_input]
    puzzle_input.sort()

    one_volt_difference = 0
    three_volt_difference = 0

    first_difference = puzzle_input[0] - 0
    if first_difference == 1:
        one_volt_difference += 1
    elif first_difference == 3:
        three_volt_difference += 1
    
    for puzzle_index in range(1, len(puzzle_input)):
        difference = puzzle_input[puzzle_index] - puzzle_input[puzzle_index - 1]
        if difference == 1:
            one_volt_difference += 1
        elif difference == 3:
            three_volt_difference += 1
        else:
            pass

    # last adapter is always a 3 volt diff with phone
    three_volt_difference += 1

    print(one_volt_difference, three_volt_difference)
    print(one_volt_difference * three_volt_difference)