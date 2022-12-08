def is_tree_visible(puzzle_input, current_location):
    neighbors_list = list()
    x, y = current_location

    # get all vertically above neighbors
    neighbors_list.append([neighbor[y] for neighbor in puzzle_input[0:x]])

    # get all vertically below neighbors
    neighbors_list.append([neighbor[y] for neighbor in puzzle_input[x + 1 :]])

    # get all horizontally left neighbors
    neighbors_list.append(puzzle_input[x][0:y])

    # get all horizontally right neighbors
    neighbors_list.append(puzzle_input[x][y + 1 :])

    # for each row compare to
    for neighbors in neighbors_list:
        is_tree_visible = True
        for neighbor in neighbors:
            if puzzle_input[x][y] <= neighbor:
                is_tree_visible = False
            if not is_tree_visible:
                break

        if is_tree_visible:
            return True
    return False


puzzle_input = list()
result = 0

with open("input.txt", "r") as puzzle_input_file:
    for line in puzzle_input_file:
        puzzle_input.append([letter for letter in line.strip()])

# add the edges as default visible
result += 2 * len(puzzle_input) + 2 * (len(puzzle_input[0]))

# remove 4 as the corners are all added twice
result -= 4


# iterate through the inner trees

for x in range(1, len(puzzle_input) - 1):
    for y in range(1, len(puzzle_input[x]) - 1):
        # check all neighbors to determine if this is visible
        # from atleast one side
        if is_tree_visible(puzzle_input, (x, y)):
            result += 1

print(result)
