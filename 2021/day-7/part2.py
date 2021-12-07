puzzle_input_list = []

with open("input.txt", "r") as puzzle_input:
    for line in puzzle_input:
        line = line.strip()
        puzzle_input_list = [int(position) for position in line.split(",")]

minimum_position = min(puzzle_input_list)
maximum_position = max(puzzle_input_list)
minimum_fuel = None

for position_goal in range(minimum_position, maximum_position+1):
    fuel = 0
    for position in puzzle_input_list:
        current_fuel = sum([number for number in range(abs(position_goal - position)+1)])
        fuel += current_fuel
        print(f"Moving from {position} to {position_goal} costs: {current_fuel}")
    print(f"Moving to {position_goal} costs: {fuel}")
    print(f"\n\n")
    if minimum_fuel is None:
        minimum_fuel = fuel
    else:
        minimum_fuel = min(minimum_fuel, fuel)

print(minimum_fuel)
