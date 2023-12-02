running_sum = 0

with open("input.txt", "r") as puzzle_input:
    lines = puzzle_input.readlines()

    for line in lines:
        line = line.strip()