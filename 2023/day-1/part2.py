puzzle_input_list = []
running_sum = 0

with open("input.txt", "r") as puzzle_input:
    lines = puzzle_input.readlines()
    puzzle_input_list = [line.strip() for line in lines]
    running_sum = 0
    
    for input_line in puzzle_input_list:
        first_digit = None
        second_digit = None
        valid_number_words = ("one", "two", "three", "four", "five", "six", "seven", "eight", "nine")
        max_count = len(input_line)
        character_index = 0
        while character_index < max_count:
            character = input_line[character_index]
            if character.isdigit():
                if first_digit is None:
                    first_digit = character
                else:
                    second_digit = character
            else:
                for number, number_word in enumerate(valid_number_words):
                    if input_line[character_index:].startswith(number_word):
                        if first_digit is None:
                            first_digit = str(number + 1)
                        else:
                            second_digit = str(number + 1)
                        
                        break
            
            character_index += 1

        if second_digit is None:
            second_digit = first_digit

        current_number = int(first_digit + second_digit)
        running_sum += current_number

    print(running_sum)