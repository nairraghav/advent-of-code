def find_combinations(puzzle_input):
    unnecessary_numbers = []
    index = 1
    while index < len(puzzle_input) - 1:
        if puzzle_input[index+1] - puzzle_input[index-1] <= 3:
            unnecessary_numbers.append(puzzle_input[index])
            del puzzle_input[index]
        else:
            index += 1

    print(unnecessary_numbers)
    print(2 ** len(unnecessary_numbers))


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

"""
1, 4, 5, 6, 7, 10, 11, 12, 15, 16, 19
Unnecessary = 5, 6, 11,
"""
