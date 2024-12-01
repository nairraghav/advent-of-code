puzzle_input_list_one = []
puzzle_input_list_two = []
running_sum = 0

with open("input.txt", "r") as puzzle_input:
    lines = puzzle_input.readlines()
    puzzle_input_list = [line.strip() for line in lines]
    
    
    for input_line in puzzle_input_list:
        a, b = input_line.split()
        a = int(a)
        b = int(b)
        puzzle_input_list_one.append(a)
        puzzle_input_list_two.append(b)

    puzzle_input_list_one.sort()
    puzzle_input_list_two.sort()
    

    for index in range(len(puzzle_input_list_one)):
        running_sum += abs(puzzle_input_list_two[index] - puzzle_input_list_one[index])
    
    print(running_sum)