houses_visited = {(0,0)}
santa_current_house = [0,0]
robot_santa_current_house = [0,0]

with open("input.txt", "r") as puzzle_input:
	for line in puzzle_input:
		for character_index in range(len(line)):
			if line[character_index] == "^":
				if character_index  % 2 == 0:
					santa_current_house[1] += 1
				else:
					robot_santa_current_house[1] += 1
			elif line[character_index] == ">":
				if character_index  % 2 == 0:
					santa_current_house[0] += 1
				else:
					robot_santa_current_house[0] += 1
			elif line[character_index] == "v":
				if character_index  % 2 == 0:
					santa_current_house[1] -= 1
				else:
					robot_santa_current_house[1] -= 1
			elif line[character_index] == "<":
				if character_index  % 2 == 0:
					santa_current_house[0] -= 1
				else:
					robot_santa_current_house[0] -= 1
			
			houses_visited.add((santa_current_house[0], santa_current_house[1]))
			houses_visited.add((robot_santa_current_house[0], robot_santa_current_house[1]))

print(len(houses_visited))
