puzzle_input_list = []
running_sum = 0

with open("input.txt", "r") as puzzle_input:
    lines = puzzle_input.readlines()
    puzzle_input_list = [line.strip() for line in lines]
    
    
    for input_line in puzzle_input_list:
        first_digit = None
        second_digit = None
        for character in input_line:
            if character.isdigit():
                if first_digit is None:
                    first_digit = character
                else:
                    second_digit = character
        if second_digit is None:
            second_digit = first_digit

        current_number = int(first_digit + second_digit)
        running_sum += current_number

    print(running_sum)