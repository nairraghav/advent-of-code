number_of_stacks = 9
number_of_vertical_stacks = 8

starting_stacks = [[] for _ in range(number_of_stacks)]
instructions = []
counter = 0

with open("input.txt", "r") as puzzle_input:
    line_counter = 0
    for line in puzzle_input:
        if line_counter < number_of_vertical_stacks:
            for index in range(number_of_stacks):
                current_stack = line[1 + index*4].strip()
                if current_stack:
                    starting_stacks[index].append(current_stack)

        else:
            if not line.startswith("move"):
                continue

            # move instructions
            instructions.append(line.strip())

        line_counter += 1

for instruction in instructions:
    _, amount_to_move, _, source, _, dest = instruction.split()
    amount_to_move = int(amount_to_move)
    # subtracting 1 since these are not 0 based
    source = int(source) - 1
    dest = int(dest) - 1
    
    print(amount_to_move, source, dest)
    items_to_move = list()
    for _ in range(amount_to_move):
        items_to_move.append(starting_stacks[source].pop(0))
    
    starting_stacks[dest][0:0] = items_to_move

print(starting_stacks)
answer = [stack[0] for stack in starting_stacks]
print("".join(answer))