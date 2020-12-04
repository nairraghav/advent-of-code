ribbon_needed = 0

with open("input.txt", "r") as puzzle_input:
	for line in puzzle_input:
		length, width, height = [int(item) for item in line.split("x")]

		dimensions = [length, width, height]
		smallest_side = min(dimensions)
		dimensions.remove(smallest_side)
		second_smallest_side = min(dimensions)
		
		ribbon_needed += 2*smallest_side + 2*second_smallest_side + length*width*height
		

print(ribbon_needed)
