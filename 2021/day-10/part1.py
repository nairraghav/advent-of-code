puzzle_input_list = []

with open("input.txt", "r") as puzzle_input:
    for line in puzzle_input:
        line = line.strip()
        puzzle_input_list.append(line)

open_brackets = {"{", "(", "[", "<"}
bracket_mapping = {"}": "{", ")": "(", "]": "[", ">": "<"}
invalid_bracket_to_points = {")": 3, "]": 57, "}": 1197, ">": 25137}
invalid_brackets = []
for puzzle_line in puzzle_input_list:
    brackets = []
    for bracket in puzzle_line:
        if bracket in open_brackets:
            brackets.append(bracket)
        else:
            if brackets[-1] == bracket_mapping[bracket]:
                del brackets[-1]
            else:
                invalid_brackets.append(bracket)
                break

print(invalid_brackets)

invalid_points = 0
for invalid_bracket in invalid_brackets:
    invalid_points += invalid_bracket_to_points[invalid_bracket]

print(invalid_points)