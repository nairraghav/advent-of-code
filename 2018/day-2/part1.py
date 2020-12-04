wrapping_paper_needed = 0

with open("input.txt", "r") as puzzle_input:
	for line in puzzle_input:
		length, width, height = [int(item) for item in line.split("x")]
		length_width = length*width
		length_height = length*height
		width_height = width*height
		
		wrapping_paper_needed += (2*length_width) + (2*length_height) + (2*width_height) + min(length_width, length_height, width_height)
		

print(wrapping_paper_needed)
