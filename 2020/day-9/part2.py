answer = 1639024365


with open("input.txt", "r") as puzzle_input:
    puzzle_input = [int(line.strip()) for line in puzzle_input]

valid_answers = []
for start_index in range(len(puzzle_input) - 1):
    for end_index in range(start_index+1, len(puzzle_input)):
        sub_list = puzzle_input[start_index:end_index]
        #print(sub_list)
        total_sum = sum(sub_list)
        if total_sum > answer:
            break

        if total_sum == answer:
            valid_answers.append(min(sub_list)+max(sub_list))

print(valid_answers[0])
