def get_neighbors(coordinates, max_rows, max_cols):
    row, col = coordinates
    has_above = row >= 1
    has_below = (max_rows - row) >= 2
    has_right = (max_cols - col) >= 2
    has_left = col >= 1
    neighbors = list()
    
    if has_above and has_left and has_right and has_below:
        neighbors.append((((row - 1, col - 1), (row, col), (row + 1, col + 1)), ((row - 1, col + 1), (row, col), (row + 1, col - 1)), ((row + 1, col - 1), (row, col), (row - 1, col + 1)), ((row + 1, col + 1), (row, col), (row - 1, col - 1))))
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
            if lines[row][col] == "A":
                for potential_straight_neighbors in neighbors:
                    neighbor_sum = 0
                    for straight_neighbors in potential_straight_neighbors:
                        xmas_string = ""
                        
                        for neighbor in straight_neighbors:
                            neighbor_row, neighbor_col = neighbor
                            xmas_string += lines[neighbor_row][neighbor_col]
                        
                        if xmas_string == "MAS":
                            neighbor_sum += 1
                    if neighbor_sum == 2:
                        running_sum += 1
        

    print(running_sum)