puzzle_input_list = []

with open("input.txt", "r") as puzzle_input:
    for line in puzzle_input:
        line = line.strip()
        puzzle_input_list = [int(state) for state in line.split(",")]

states = dict()
for state in puzzle_input_list:
    states[state] = states.get(state, 0) + 1

for _ in range(80):
    new_states = dict()
    for index in range(9):
        state = states.get(index, 0)
        if index == 0:
            new_states[8] = state
            new_states[6] = new_states.get(6, 0) + state
        else:
            new_states[index - 1] = new_states.get(index - 1, 0) + state
    states = new_states

number_of_fish = 0
for state in states:
    number_of_fish += states[state]

print(number_of_fish)
