def get_neighbors(row_index, column_index, length, width):
    neighbors = []
    for neighbor_row_index, neighbor_column_index in [(row_index-1, column_index-1), (row_index-1, column_index), (row_index-1, column_index+1), (row_index, column_index-1), (row_index, column_index+1), (row_index+1, column_index-1), (row_index-1, column_index), (row_index-1, column_index+1)]:
        if 0 <= neighbor_row_index < length and 0 <= neighbor_column_index < width:
            neighbors.append((neighbor_row_index, neighbor_column_index))

    return neighbors


puzzle_input_list = []

with open("input.txt", "r") as puzzle_input:
    for line in puzzle_input:
        line = line.strip()
        puzzle_input_list.append([int(digit) for digit in line])

total_flashes = 0
width = len(puzzle_input_list)
for _ in range(100):
    flashed_indices = []
    for row_index in range(width):
        length = len(puzzle_input_list[row_index])
        for column_index in range(length):
            if puzzle_input_list[row_index][column_index] < 9:
                puzzle_input_list[row_index][column_index] += 1
            elif puzzle_input_list[row_index][column_index] == 9:
                flashed_indices.append((row_index, column_index))
                puzzle_input_list[row_index][column_index] = 0

    already_flashed = set()
    while flashed_indices:
        flashed_row_index, flashed_column_index = flashed_indices.pop(0)
        already_flashed.add((flashed_row_index, flashed_column_index))
        total_flashes += 1
        neighbors = get_neighbors(flashed_row_index, flashed_column_index, length, width)
        for neighbor_row_index, neighbor_column_index in neighbors:
            if (neighbor_row_index, neighbor_column_index) not in already_flashed:
                if puzzle_input_list[neighbor_row_index][neighbor_column_index] == 9:
                    puzzle_input_list[neighbor_row_index][neighbor_column_index] = 0
                    flashed_indices.append((neighbor_row_index, neighbor_column_index))
                else:
                    puzzle_input_list[neighbor_row_index][neighbor_column_index] += 1

import pprint
pprint.pprint(puzzle_input_list)
print(total_flashes)