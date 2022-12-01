puzzle_input_list = []
current_count = 0

with open("input.txt", "r") as puzzle_input:

    for line in puzzle_input:
        try:
            current_count += int(line)
        except ValueError:
            puzzle_input_list.append(current_count)
            current_count = 0

    puzzle_input_list.append(current_count)

# sort the list to get them in order
puzzle_input_list = sorted(puzzle_input_list)

# return the sum of the last (greatest) 3
print(sum(puzzle_input_list[-3:]))
