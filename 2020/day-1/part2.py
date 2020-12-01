puzzle_input_list = []

with open("part_1_input.txt", "r") as puzzle_input:
	for line in puzzle_input:
		puzzle_input_list.append(int(line))


list_length = len(puzzle_input_list)

for first_number in range(list_length):
	for second_number in range(first_number, list_length):
		for third_number in range(second_number, list_length):
			if puzzle_input_list[first_number] + puzzle_input_list[second_number] + puzzle_input_list[third_number] == 2020:
				print(f"{puzzle_input_list[first_number]} * {puzzle_input_list[second_number]} * {puzzle_input_list[third_number]} = {puzzle_input_list[first_number] * puzzle_input_list[second_number] * puzzle_input_list[third_number]}")
				break