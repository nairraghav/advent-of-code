def get_questions_answered_for_groups(group_answers) -> int:
    answers = set()
    for line in group_answers.split(" "):
        for answer in line:
            if answer not in answers:
                answers.add(answer)
    return len(answers)
    

group_answers = ""
sum_of_questions_answered = 0
with open("input.txt", "r") as puzzle_input:
    for line in puzzle_input:
        line = line.strip()
        if len(line) == 0:
            sum_of_questions_answered += get_questions_answered_for_groups(group_answers.strip())
            group_answers = ""
        else:
            group_answers += f" {line}"

    sum_of_questions_answered += get_questions_answered_for_groups(group_answers.strip())

print(sum_of_questions_answered)
