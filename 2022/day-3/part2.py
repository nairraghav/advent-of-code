puzzle_input_list = []
running_total = 0

with open("input.txt", "r") as puzzle_input:

    for line in puzzle_input:
        line = line.strip()
        puzzle_input_list.append(line)


for index in range(0, len(puzzle_input_list), 3):
    first_rucksack = puzzle_input_list[index]
    second_rucksack = puzzle_input_list[index + 1]
    third_rucksack = puzzle_input_list[index + 2]

    first_unique_rucksack = {letter for letter in first_rucksack}
    second_unique_rucksack = {letter for letter in second_rucksack}
    third_unique_rucksack = {letter for letter in third_rucksack}

    common_values = list(
        {
            letter
            for letter in first_unique_rucksack
            if letter in second_unique_rucksack and letter in third_unique_rucksack
        }
    )

    matched_letter = common_values[0]

    is_upper = matched_letter.isupper()
    running_total += ord(matched_letter.lower()) - 96

    if is_upper:
        running_total += 26

print(running_total)
