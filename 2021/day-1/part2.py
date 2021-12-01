puzzle_input_list = list()

with open("input.txt", "r") as puzzle_input:
    for line in puzzle_input:
        puzzle_input_list.append(int(line))

depths_list = list()
for index in range(0, len(puzzle_input_list) - 2):
    depths_list.append(sum(puzzle_input_list[index:index+3]))

greater_than_previous_count = 0
for index in range(1, len(depths_list)):
    if depths_list[index] > depths_list[index-1]:
        greater_than_previous_count += 1

print(greater_than_previous_count)