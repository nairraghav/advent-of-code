available_marbles = {"red", "green", "blue"}
running_sum = 0

with open("input.txt", "r") as puzzle_input:
    lines = puzzle_input.readlines()

    for line in lines:
        line = line.strip()
        game_info, cube_info = line.split(":")
        game_id = int(game_info.split()[-1])
        valid_round_count = 0
        marble_counts = dict()

        for round in cube_info.split(";"):
            valid_round = True

            for marble_info in round.split(","):
                marble_info = marble_info.strip()
                marble_count, marble_type = marble_info.split()
                marble_count = int(marble_count)
                marble_counts[marble_type] = max(
                    marble_counts.get(marble_type, 0), marble_count
                )

        power_of_set = 1
        for marble_type in available_marbles:
            power_of_set *= marble_counts.get(marble_type, 0)

        running_sum += power_of_set

    print(running_sum)
