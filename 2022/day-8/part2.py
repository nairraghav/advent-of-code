def get_scenic_score(puzzle_input, current_location):
    neighbors_list = list()
    x, y = current_location

    # get all vertically above neighbors (need to reverse the order here)
    neighbors_list.append([neighbor[y] for neighbor in puzzle_input[0:x]][::-1])

    # get all vertically below neighbors
    neighbors_list.append([neighbor[y] for neighbor in puzzle_input[x + 1 :]])

    # get all horizontally left neighbors (need to reverse order here)
    neighbors_list.append(puzzle_input[x][0:y][::-1])

    # get all horizontally right neighbors
    neighbors_list.append(puzzle_input[x][y + 1 :])

    score = 1
    # for each row compare to
    for neighbors in neighbors_list:
        tree_count = 0
        for neighbor in neighbors:
            tree_count += 1
            if puzzle_input[x][y] <= neighbor:
                break
        score *= tree_count

    return score


puzzle_input = list()
result = list()

with open("input.txt", "r") as puzzle_input_file:
    for line in puzzle_input_file:
        puzzle_input.append([letter for letter in line.strip()])

# iterate through the inner trees and calculate tree scores
for x in range(1, len(puzzle_input) - 1):
    for y in range(1, len(puzzle_input[x]) - 1):
        # check all neighbors to determine if this is visible
        # from atleast one side
        result.append(get_scenic_score(puzzle_input, (x, y)))

print(max(result))
