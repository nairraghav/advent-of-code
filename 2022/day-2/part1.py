puzzle_input_list = []

pick_score = {"X": 1, "Y": 2, "Z": 3}

total_score = 0


def get_round_score(opponent_pick, my_pick):
    if opponent_pick == "A":
        if my_pick == "X":
            return 3
        elif my_pick == "Y":
            return 6
        else:
            return 0

    if opponent_pick == "B":
        if my_pick == "X":
            return 0
        elif my_pick == "Y":
            return 3
        else:
            return 6

    if my_pick == "X":
        return 6
    elif my_pick == "Y":
        return 0
    else:
        return 3


with open("input.txt", "r") as puzzle_input:

    for line in puzzle_input:
        opponent_pick, my_pick = line.split()
        total_score += pick_score[my_pick] + get_round_score(
            opponent_pick, my_pick
        )


print(total_score)
