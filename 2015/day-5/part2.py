def get_repeat_dict_from_string(string) -> dict:
	repeat_dict = {}
	for letter_index in range(len(string) - 1):
		if f"{string[letter_index]}{string[letter_index+1]}" in repeat_dict:
			repeat_dict[f"{string[letter_index]}{string[letter_index+1]}"].append(letter_index)
		else:
			repeat_dict[f"{string[letter_index]}{string[letter_index+1]}"] = [letter_index]

	return repeat_dict

def is_nice_string(string) -> bool:
	repeating_letters_with_one_letter_in_middle = False
	for letter_index in range(len(string) - 2):
		if string[letter_index] == string[letter_index + 2]:
			repeating_letters_with_one_letter_in_middle = True
			break
	
	if not repeating_letters_with_one_letter_in_middle:
		return False

	repeat_dict = get_repeat_dict_from_string(string)

	for _, values in repeat_dict.items():
		if len(values) > 2:
			return True

		if len(values) == 2:
			if values[0] != values[1] - 1:
				return True

	return False


nice_strings_count = 0

with open("input.txt", "r") as puzzle_input:
	for line in puzzle_input:
		if is_nice_string(line.strip()):
			nice_strings_count += 1

print(nice_strings_count)
