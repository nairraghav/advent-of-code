
with open("input.txt", "r") as puzzle_input:

    puzzle_input = [line.strip() for line in puzzle_input]
    busses_input = puzzle_input[1].split(",")
    busses = []
    for bus_input in busses_input:
        if bus_input != "x":
            busses.append(int(bus_input))
        else:
            busses.append("x")
