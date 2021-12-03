puzzle_input_list = []

with open("input.txt", "r") as puzzle_input:
    for line in puzzle_input:
        puzzle_input_list.append(line)

aim = 0
horizontal_position = 0
vertical_position = 0

for command in puzzle_input_list:
    direction, amount = command.split()
    amount = int(amount)
    if direction == "forward":
        horizontal_position += amount
        vertical_position += aim * amount
    elif direction == "up":
        aim -= amount
    elif direction == "down":
        aim += amount
    else:
        raise Exception(f"Invalid Direction: {direction}")

print(f"Horizontal Position: {horizontal_position}")
print(f"Vertical Position: {vertical_position}")
print(horizontal_position * vertical_position)