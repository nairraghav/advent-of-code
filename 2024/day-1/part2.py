puzzle_input_list_one = list()
puzzle_input_list_two = dict()
running_sum = 0

with open("input.txt", "r") as puzzle_input:
    lines = puzzle_input.readlines()
    puzzle_input_list = [line.strip() for line in lines]
    
    
    for input_line in puzzle_input_list:
        a, b = input_line.split()
        a = int(a)
        b = int(b)
        puzzle_input_list_one.append(a)
        puzzle_input_list_two[b] = puzzle_input_list_two.get(b, 0) + 1    

    for index in range(len(puzzle_input_list_one)):
        running_sum += puzzle_input_list_one[index] * puzzle_input_list_two.get(puzzle_input_list_one[index], 0)
    
    print(running_sum)