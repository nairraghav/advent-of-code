def get_neighbors(row_index, column_index, width, length):
    neighbors = []
    if row_index - 1 >= 0:
        neighbors.append((row_index - 1, column_index))

    if row_index + 1 < width:
        neighbors.append((row_index + 1, column_index))

    if column_index - 1 >= 0:
        neighbors.append((row_index, column_index - 1))

    if column_index + 1 < length:
        neighbors.append((row_index, column_index + 1))

    return neighbors


puzzle_input_list = []

with open("input.txt", "r") as puzzle_input:
    for line in puzzle_input:
        line = line.strip()
        current_row = [int(digit) for digit in line]
        puzzle_input_list.append(current_row)

low_points = []
for row_index in range(len(puzzle_input_list)):
    for column_index in range(len(puzzle_input_list[row_index])):
        neighbors = get_neighbors(row_index, column_index, len(puzzle_input_list), len(puzzle_input_list[row_index]))
        low_point = True
        for neighbor_row_index, neighbor_column_index in neighbors:
            if low_point is False:
                break

            if puzzle_input_list[row_index][column_index] >= puzzle_input_list[neighbor_row_index][neighbor_column_index]:
                low_point = False

        if low_point is True:
            low_points.append(puzzle_input_list[row_index][column_index])

print(low_points)
print(sum(low_points) + len(low_points))
