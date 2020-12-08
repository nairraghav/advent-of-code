puzzle = []
with open("input.txt", "r") as puzzle_input:
    for line in puzzle_input:
        puzzle.append(line.strip())


def get_accumulator_value(puzzle) -> (bool,int):
    accumulator = 0
    puzzle_index = 0
    visited_indices = set()
    while puzzle_index < len(puzzle):
        if puzzle_index not in visited_indices:
            visited_indices.add(puzzle_index)
        else:
            return False, accumulator

        action = puzzle[puzzle_index][:3]
        number = int(puzzle[puzzle_index][4:])
        if action == "jmp":
            puzzle_index += number
        else:
            if action == "acc":
                accumulator += number

            puzzle_index += 1
    return True, accumulator

for puzzle_index in range(len(puzzle)):
    if puzzle[puzzle_index][:3] == "jmp":
        old_value = puzzle[puzzle_index]
        puzzle[puzzle_index] = "nop" + puzzle[puzzle_index][3:]
        passed, accumulator = get_accumulator_value(puzzle)
    elif puzzle[puzzle_index][:3] == "nop":
        old_value = puzzle[puzzle_index]
        puzzle[puzzle_index] = "jmp" + puzzle[puzzle_index][3:]
        passed, accumulator = get_accumulator_value(puzzle)
    else:
        passed = False
        old_value = None

    if passed:
        break
    
    if old_value is not None:
        puzzle[puzzle_index] = old_value


print(accumulator)