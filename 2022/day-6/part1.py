puzzle_input = list()
message_marker_length = 4
result = None

with open("input.txt", "r") as puzzle_input_file:
    for line in puzzle_input_file:
        puzzle_input = line

for index in range(len(puzzle_input) - message_marker_length):
    subset = puzzle_input[index : index + message_marker_length]
    subset_counter = {letter for letter in subset}
    if len(subset_counter) == message_marker_length:
        result = index + message_marker_length
        break

print(result)
