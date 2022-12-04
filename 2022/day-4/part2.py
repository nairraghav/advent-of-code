puzzle_input_list = []
counter = 0

with open("input.txt", "r") as puzzle_input:

    for line in puzzle_input:
        line = line.strip()
        first_range, second_range = line.split(",")
        fully_contained = False
        
        
        first_range_first_number, first_range_second_number = first_range.split("-")
        second_range_first_number, second_range_second_number = second_range.split("-")

        # get ranges in integers
        first_range = [int(first_range_first_number), int(first_range_second_number)]
        second_range = [int(second_range_first_number), int(second_range_second_number)]
        
        if first_range[0] >= second_range[0] and first_range[0] <= second_range[1]:
            counter += 1
            continue
        
        if first_range[1] >= second_range[0] and first_range[1] <= second_range[1]:
            counter += 1
            continue
        
        if second_range[0] >= first_range[0] and second_range[0] <= first_range[1]:
            counter += 1
            continue
        
        if second_range[1] >= first_range[0] and second_range[1] <= first_range[1]:
            counter += 1
            continue
        
print(counter)