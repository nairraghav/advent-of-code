puzzle_input = list()
cycle = 0
important_cycles = {20, 60, 100, 140, 180, 220}
x_value = 1
cycles_and_values = dict()
result = list()


with open("input.txt", "r") as puzzle_input_file:
    for line in puzzle_input_file:
        line = line.strip()

        cycle += 1
        if line.startswith("noop"):
            operation = "noop"

            cycles_and_values[cycle] = x_value
        else:
            operation, value = line.split()
            value = int(value)

            cycles_and_values[cycle] = x_value
            cycle += 1
            cycles_and_values[cycle] = x_value
            x_value += value

for cycle_index in range(1, 241):
    cycle_value = cycles_and_values[cycle_index]
    sprite_positions = {cycle_value - 1, cycle_value, cycle_value + 1}
    current_crt_position = cycle_index - 1
    current_crt_position %= 40
    if current_crt_position in sprite_positions:
        result.append("#")
    else:
        result.append(".")

result = [
    result[0:40],
    result[40:80],
    result[80:120],
    result[120:160],
    result[160:200],
    result[200:240],
]
for line in result:
    print(line)
