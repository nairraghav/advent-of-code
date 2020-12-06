def get_questions_answered_by_all_for_groups(group_answers) -> int:
    answers = {}
    person_count = 0
    for line in group_answers.split(" "):
        person_count += 1
        for answer in line:
            if answer in answers:
                answers[answer].append(person_count)
            else:
                answers[answer] = [person_count]

    number_of_answers_answered_by_all = 0
    for answer in answers:
        if len(answers[answer]) == person_count:
            number_of_answers_answered_by_all += 1

    return number_of_answers_answered_by_all
    

group_answers = ""
sum_of_same_questions_answered_by_all = 0
with open("input.txt", "r") as puzzle_input:
    for line in puzzle_input:
        line = line.strip()
        if len(line) == 0:
            sum_of_same_questions_answered_by_all += get_questions_answered_by_all_for_groups(group_answers.strip())
            group_answers = ""
        else:
            group_answers += f" {line}"

    sum_of_same_questions_answered_by_all += get_questions_answered_by_all_for_groups(group_answers.strip())

print(sum_of_same_questions_answered_by_all)
