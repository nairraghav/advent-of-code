multiplied_trees = 1
trees_hit = 0

with open("input.txt", "r") as puzzle_input:
    horizontal_index = 0 
    for line in puzzle_input:
        line = line.strip()
        
        current_line = line * multiplied_trees
        if horizontal_index >= len(current_line):
            multiplied_trees += 1
        
        current_line = line * multiplied_trees

        if current_line[horizontal_index] == "#":
            trees_hit += 1

        horizontal_index += 3

print(trees_hit)