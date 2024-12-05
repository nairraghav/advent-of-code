def get_neighbors(coordinates, max_rows, max_cols):
    row, col = coordinates
    has_above = row >= 3
    has_below = (max_rows - row) >= 4
    has_right = (max_cols - col) >= 4
    has_left = col >= 3
    neighbors = list()
    
    if has_above:
        neighbors.append(((row, col), (row - 1, col), (row - 2, col), (row - 3, col)))
        if has_left:
            neighbors.append(((row, col), (row - 1, col - 1), (row - 2, col - 2), (row - 3, col - 3)))
        if has_right:
            neighbors.append(((row, col), (row - 1, col + 1), (row - 2, col + 2), (row - 3, col + 3)))
    if has_below:
        neighbors.append(((row, col), (row + 1, col), (row + 2, col), (row + 3, col)))
        if has_left:
            neighbors.append(((row, col), (row + 1, col - 1), (row + 2, col - 2), (row + 3, col - 3)))
        if has_right:
            neighbors.append(((row, col), (row + 1, col + 1), (row + 2, col + 2), (row + 3, col + 3)))

    if has_left:
        neighbors.append(((row, col), (row, col - 1), (row, col - 2), (row, col - 3)))

    if has_right:
        neighbors.append(((row, col), (row, col + 1), (row, col + 2), (row, col + 3)))

    return neighbors


running_sum = 0

with open("input.txt", "r") as puzzle_input:
    lines = puzzle_input.readlines()
    lines = [list(line.strip()) for line in lines]
    max_rows = len(lines)
    max_cols = len(lines[0])

    for row in range(len(lines)):
        for col in range(len(lines[row])):
            neighbors = get_neighbors((row, col), max_rows, max_cols)
            if lines[row][col] == "X":
                for straight_neighbors in neighbors:
                    xmas_string = ""
                    for neighbor in straight_neighbors:
                        neighbor_row, neighbor_col = neighbor
                        xmas_string += lines[neighbor_row][neighbor_col]
                    print(xmas_string)
                    if xmas_string == "XMAS":
                        running_sum += 1
        

    print(running_sum)