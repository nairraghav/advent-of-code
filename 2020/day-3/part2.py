def find_trees_for_horizontal_and_vertical_change(horizontal_change, vertical_change):
    multiplied_trees = 1
    trees_hit = 0
    
    with open("input.txt", "r") as puzzle_input:
        horizontal_index = 0
        vertical_index = 0
        for line in puzzle_input:
            if (vertical_index >= 1) and (vertical_index % vertical_change != 0):
                vertical_index += 1
                continue
            line = line.strip()
            
            current_line = line * multiplied_trees
            if horizontal_index >= len(current_line):
                multiplied_trees += 1
            
            current_line = line * multiplied_trees

            if current_line[horizontal_index] == "#":
                trees_hit += 1

            horizontal_index += horizontal_change
            vertical_index += 1

    print(trees_hit)
    return trees_hit

slopes_to_check = [(1,1), (3,1), (5,1), (7,1), (1,2)]

rolling_product = 1
for horizontal_change, vertical_change in slopes_to_check:
    rolling_product *= find_trees_for_horizontal_and_vertical_change(horizontal_change, vertical_change)
    print(rolling_product)
