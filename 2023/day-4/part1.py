running_sum = 0

with open("input.txt", "r") as puzzle_input:
    lines = puzzle_input.readlines()
    for line_index, line in enumerate(lines):
        line = line.strip()

    print(running_sum)