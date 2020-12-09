PREABMLE = 25


with open("input.txt", "r") as puzzle_input:
    puzzle_input = [int(line.strip()) for line in puzzle_input]

current_index = 0

for index in range(len(puzzle_input) - PREABMLE):
    sub_list = puzzle_input[index:index+PREABMLE]
    goal_index = index + PREABMLE
    is_possible = False
    for sub_index in range(PREABMLE-1):
        for sub_index_next in range(sub_index+1, PREABMLE):
            if sub_list[sub_index] != sub_list[sub_index_next]:
                if sub_list[sub_index] + sub_list[sub_index_next] == puzzle_input[goal_index]:
                    is_possible = True

    if not is_possible:
        break

print(puzzle_input[goal_index])
