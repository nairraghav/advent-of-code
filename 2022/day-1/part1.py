puzzle_input_list = []
current_count = 0

with open("input.txt", "r") as puzzle_input:
    
    for line in puzzle_input:
        try:
            current_count += int(line)
        except:
            puzzle_input_list.append(current_count)
            current_count = 0
    
    puzzle_input_list.append(current_count)
    
print(max(puzzle_input_list))