
with open("input.txt", "r") as puzzle_input:

    puzzle_input = [line.strip() for line in puzzle_input]
    earliest_time = int(puzzle_input[0])
    busses_input = puzzle_input[1].split(",")
    busses = []
    for bus_input in busses_input:
        if bus_input != "x":
            busses.append(int(bus_input))


current_time = earliest_time
is_complete = False
while not is_complete:
    for bus in busses:
        if current_time % bus == 0:
            print(current_time - earliest_time)
            print(bus)
            print((current_time - earliest_time) * bus)
            is_complete = True
    current_time += 1