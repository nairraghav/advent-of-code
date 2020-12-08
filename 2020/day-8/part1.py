accumulator = 0

puzzle = []
with open("input.txt", "r") as puzzle_input:
    for line in puzzle_input:
        puzzle.append(line.strip())

puzzle_index = 0
visited_indices = set()
while puzzle_index < len(puzzle):
    if puzzle_index not in visited_indices:
        visited_indices.add(puzzle_index)
    else:
        break

    action = puzzle[puzzle_index][:3]
    number = int(puzzle[puzzle_index][4:])
    if action == "jmp":
        puzzle_index += number
    else:
        if action == "acc":
            accumulator += number

        puzzle_index += 1

print(accumulator)