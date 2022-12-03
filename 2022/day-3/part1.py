puzzle_input_list = []
running_total = 0

with open("input.txt", "r") as puzzle_input:

    for line in puzzle_input:
        rucksack_length = len(line)
        rucksack_one = line[:rucksack_length//2]
        rucksack_two = line[rucksack_length//2:]

        unique_letters = {letter for letter in rucksack_one}
        matched_letter = None

        for letter in rucksack_two:
            if letter in unique_letters:
                matched_letter = letter
                break
            else:
                pass

        is_upper = matched_letter.isupper()
        running_total += ord(matched_letter.lower()) - 96

        if is_upper:
            running_total += 26

print(running_total)

