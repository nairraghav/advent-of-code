max_available_marbles = {"red": 12, "green": 13, "blue": 14}
running_sum = 0

with open("input.txt", "r") as puzzle_input:
    lines = puzzle_input.readlines()

    for line in lines:
        line = line.strip()
        game_info, cube_info = line.split(":")
        game_id = int(game_info.split()[-1])
        valid_round_count = 0

        for round in cube_info.split(";"):
            marble_counts = dict()
            valid_round = True

            for marble_info in round.split(","):
                marble_info = marble_info.strip()
                marble_count, marble_type = marble_info.split()
                marble_count = int(marble_count)
                marble_counts[marble_type] = max(
                    marble_counts.get(marble_type, 0), marble_count
                )

            for color in max_available_marbles:
                if max_available_marbles[color] < marble_counts.get(color, 0):
                    valid_round = False
                    break

            if not valid_round:
                break
            else:
                valid_round_count += 1

        if valid_round_count == len(cube_info.split(";")):
            running_sum += game_id

    print(running_sum)
