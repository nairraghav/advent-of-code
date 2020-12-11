def find_combinations(puzzle_input):
    explored_inputs = [puzzle_input]
    explored_set = set()
    explored_set.add(str(puzzle_input))
    for explored_input in explored_inputs:
        for index in range(len(explored_input) - 2):
            if explored_input[index+2] - explored_input[index] <= 3:
                string_input = str(explored_input[:index+1] + explored_input[index+2:])
                if string_input not in explored_set:
                    explored_set.add(string_input)
                    explored_inputs.append(explored_input[:index+1] + explored_input[index+2:])
    
    print(len(explored_set))


with open("input.txt", "r") as puzzle_input:
    puzzle_input = [int(line.strip()) for line in puzzle_input]
    puzzle_input.sort()

    find_combinations(puzzle_input)

"""
1, 4, 5, 6, 7, 10, 11, 12, 15, 16, 19 (full)
    1, 4, 5, 6, 7, 10, 12, 15, 16, 19 (remove 11)
        1, 4, 5, 7, 10, 12, 15, 16, 19 (remove 6)
        1, 4, 6, 7, 10, 12, 15, 16, 19 (remove 5)
            1, 4, 7, 10, 12, 15, 16, 19 (remove 6)
    1, 4, 5, 7, 10, 11, 12, 15, 16, 19 (remove 6)
        1, 4, 7, 10, 11, 12, 15, 16, 19 (remove 5)
    1, 4, 6, 7, 10, 11, 12, 15, 16, 19 (remove 5)
"""