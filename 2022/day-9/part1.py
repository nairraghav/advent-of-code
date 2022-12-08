puzzle_input = list()
result = 0

with open("input.txt", "r") as puzzle_input_file:
    for line in puzzle_input_file:
        puzzle_input.append(line.strip())

print(result)
