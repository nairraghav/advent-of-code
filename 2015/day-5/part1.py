def is_nice_string(string) -> bool:
	bad_strings = ("ab", "cd", "pq", "xy")
	for bad_string in bad_strings:
		if bad_string in string:
			return False

	vowel_count = 0
	vowels = ("a", "e", "i", "o", "u")
	for vowel in vowels:
		vowel_count += string.count(vowel)
		if vowel_count >= 3:
			break
	
	if vowel_count < 3:
		return False

	previous_letter = string[0]
	for letter_index in range(1,len(string)):
		if previous_letter == string[letter_index]:
			return True
		previous_letter = string[letter_index]

	return False
	


nice_strings_count = 0
with open("input.txt", "r") as puzzle_input:
	for line in puzzle_input:
		if is_nice_string(line.strip()):
			nice_strings_count += 1

print(nice_strings_count)