puzzle_input_list = []

with open("input.txt", "r") as puzzle_input:
    for line in puzzle_input:
        puzzle_input_list.append(int(line))

greater_than_previous_count = 0
for index in range(1, len(puzzle_input_list)):
    if puzzle_input_list[index] > puzzle_input_list[index-1]:
        greater_than_previous_count += 1

print(greater_than_previous_count)