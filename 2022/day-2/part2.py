puzzle_input_list = []
round_score = {"X": 0, "Y": 3, "Z": 6}
total_score = 0


def get_round_score(opponent_pick, round_decision):
    if opponent_pick == "A":
        if round_decision == "X":
            return 3
        elif round_decision == "Y":
            return 1
        else:
            return 2

    if opponent_pick == "B":
        if round_decision == "X":
            return 1
        elif round_decision == "Y":
            return 2
        else:
            return 3

    if round_decision == "X":
        return 2
    elif round_decision == "Y":
        return 3
    else:
        return 1


with open("input.txt", "r") as puzzle_input:

    for line in puzzle_input:
        opponent_pick, round_decision = line.split()
        total_score += round_score[round_decision] + get_round_score(
            opponent_pick, round_decision
        )


print(total_score)
