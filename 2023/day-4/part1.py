def get_lines_from_input_stripped():
    output_lines = list()
    with open("input.txt", "r") as puzzle_input:
        lines = puzzle_input.readlines()
        for line in lines:
            all_numbers = line.split(":")[-1]
            all_numbers = all_numbers.strip()
            winning_numbers, have_numbers = all_numbers.split("|")
            winning_numbers = winning_numbers.strip()
            have_numbers = have_numbers.strip()
            winning_numbers = {int(number) for number in winning_numbers.split()}
            have_numbers = [int(number) for number in have_numbers.split()]
            output_lines.append((winning_numbers, have_numbers))
        
    return output_lines

def main():
    running_sum = 0
    lines = get_lines_from_input_stripped()
    for winning_numbers, have_numbers in lines:
        number_matches = 0
        for number in have_numbers:
            if number in winning_numbers:
                number_matches += 1
        if number_matches > 0:
            running_sum += 2**(number_matches - 1)
    
    print(running_sum)

if __name__ == "__main__":
    main()