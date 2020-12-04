houses_visited = {(0,0)}
current_house = [0,0]

with open("input.txt", "r") as puzzle_input:
	for line in puzzle_input:
		for character in line:
			if character == "^":
				current_house[1] += 1
			elif character == ">":
				current_house[0] += 1
			elif character == "v":
				current_house[1] -= 1
			elif character == "<":
				current_house[0] -= 1
			
			houses_visited.add((current_house[0], current_house[1]))

print(len(houses_visited))
