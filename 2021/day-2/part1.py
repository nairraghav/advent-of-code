puzzle_input_list = []

with open("input.txt", "r") as puzzle_input:
    for line in puzzle_input:
        puzzle_input_list.append(line)

horizontal_position = 0
vertical_position = 0

for command in puzzle_input_list:
    direction, amount = command.split()
    amount = int(amount)
    if direction == "forward":
        horizontal_position += amount
    elif direction == "up":
        vertical_position -= amount
    elif direction == "down":
        vertical_position += amount
    else:
        raise Exception(f"Invalid Direction: {direction}")

print(f"Horizontal Position: {horizontal_position}")
print(f"Vertical Position: {vertical_position}")
print(horizontal_position * vertical_position)