# incorrect solution
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
width = len(puzzle_input_list)
length = 0
for row_index in range(len(puzzle_input_list)):
    for column_index in range(len(puzzle_input_list[row_index])):
        length = len(puzzle_input_list[row_index])
        neighbors = get_neighbors(row_index, column_index, width, length)
        low_point = True
        for neighbor_row_index, neighbor_column_index in neighbors:
            if low_point is False:
                break

            if puzzle_input_list[row_index][column_index] >= puzzle_input_list[neighbor_row_index][neighbor_column_index]:
                low_point = False

        if low_point is True:
            low_points.append((row_index,column_index))

# for each low point, determine basin length (DFS out and get size of island)
basin_sizes = []
for row_index, column_index in low_points:
    basin_size = 0
    indices_to_visit = [(row_index, column_index)]
    visited_indices = set()
    while indices_to_visit:
        row_index_to_visit, column_index_to_visit = indices_to_visit[0]
        if (row_index_to_visit, column_index_to_visit) not in visited_indices:
            basin_size += 1
            visited_indices.add((row_index_to_visit, column_index_to_visit))
            if puzzle_input_list[row_index_to_visit][column_index_to_visit] <= 7:
                neighbors = get_neighbors(row_index_to_visit, column_index_to_visit, width, length)
                for neighbor_row_index, neighbor_column_index in neighbors:
                    if (neighbor_row_index, neighbor_column_index) in visited_indices:
                        continue
                    
                    if puzzle_input_list[neighbor_row_index][neighbor_column_index] - puzzle_input_list[row_index_to_visit][column_index_to_visit] == 1:
                        indices_to_visit.append((neighbor_row_index, neighbor_column_index))
        del indices_to_visit[0]
    basin_sizes.append(basin_size)

# determine 3 largest basins
basin_sizes.sort(reverse=True)
print(basin_sizes)
# return product of 3 largest basin sizes
print(basin_sizes[0] * basin_sizes[1] * basin_sizes[2])
