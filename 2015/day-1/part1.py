current_floor = 0

with open("input.txt", "r") as puzzle_input:
	for line in puzzle_input:
		for character in line:
			if character == "(":
				current_floor += 1
			elif character == ")":
				current_floor -= 1
			else:
				pass

print(current_floor)