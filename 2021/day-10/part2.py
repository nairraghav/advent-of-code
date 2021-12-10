puzzle_input_list = []

with open("input.txt", "r") as puzzle_input:
    for line in puzzle_input:
        line = line.strip()
        puzzle_input_list.append(line)

open_brackets = {"{", "(", "[", "<"}
bracket_mapping = {"}": "{", ")": "(", "]": "[", ">": "<",
                   "{": "}", "(": ")", "[": "]", "<": ">"
                   }
bracket_to_points = {")": 1, "]": 2, "}": 3, ">": 4}
incomplete_lines = []

for puzzle_line in puzzle_input_list:
    brackets = []
    valid_line = True
    for bracket in puzzle_line:
        if bracket in open_brackets:
            brackets.append(bracket)
        else:
            if brackets[-1] == bracket_mapping[bracket]:
                del brackets[-1]
            else:
                valid_line = False

    if valid_line is True:
        incomplete_lines.append(brackets)

scores = []
for incomplete_line in incomplete_lines:
    score = 0
    for character in incomplete_line[::-1]:
        score *= 5
        score += bracket_to_points[bracket_mapping[character]]
    scores.append(score)

scores.sort()
print(scores)
print(scores[len(scores)//2])
