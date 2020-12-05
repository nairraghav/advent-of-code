def find_binary_partitioned_seat(seat_range, input_text):
    for letter in input_text:
        difference = abs(seat_range[0] - seat_range[1]) // 2
        if (letter == "F") or (letter == "L"):
            seat_range = [seat_range[0], seat_range[0] + difference]
        else:
            seat_range = [seat_range[1] - difference, seat_range[1]]

    assert seat_range[0] == seat_range[1]
    return(seat_range[0])


with open("input.txt", "r") as puzzle_input:
    highest_seat_id = 0
    for line in puzzle_input:
        line = line.strip()

        vertical_seat_input = line[:-3]
        horizontal_seat_input = line[-3:]

        vertical_seat = find_binary_partitioned_seat([0, 127], vertical_seat_input)
        horizontal_seat = find_binary_partitioned_seat([0, 7], horizontal_seat_input)

        highest_seat_id = max(highest_seat_id, vertical_seat * 8 + horizontal_seat)

    print(highest_seat_id)
