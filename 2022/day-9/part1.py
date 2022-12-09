def determine_new_tail_location(header_location, tail_location):
    # same x axis
    if header_location[0] == tail_location[0]:
        difference = header_location[1] - tail_location[1]
        if difference > 1:
            tail_location[1] += 1
        elif difference < -1:
            tail_location[1] -= 1
        else:
            pass
    # same y axis
    elif header_location[1] == tail_location[1]:
        difference = header_location[0] - tail_location[0]
        if difference > 1:
            tail_location[0] += 1
        elif difference < -1:
            tail_location[0] -= 1
        else:
            pass
        return tail_location

    # diagonal relationship
    else:
        x_difference = header_location[0] - tail_location[0]
        y_difference = header_location[1] - tail_location[1]
        if x_difference > 1:
            tail_location[0] += 1
            if y_difference > 0:
                tail_location[1] += 1
            else:
                tail_location[1] -= 1
            return tail_location
        elif x_difference < -1:
            tail_location[0] -= 1
            if y_difference > 0:
                tail_location[1] += 1
            else:
                tail_location[1] -= 1
            return tail_location
        if y_difference > 1:
            tail_location[1] += 1
            if x_difference > 0:
                tail_location[0] += 1
            else:
                tail_location[0] -= 1
            return tail_location
        elif y_difference < -1:
            tail_location[1] -= 1
            if x_difference > 0:
                tail_location[0] += 1
            else:
                tail_location[0] -= 1
            return tail_location
    
    return tail_location


puzzle_input = list()
header_location = [0, 0]
tail_location = [0, 0]
visited_tail_locations = set()
visited_tail_locations.add(tuple(tail_location))

with open("input.txt", "r") as puzzle_input_file:
    for line in puzzle_input_file:
        puzzle_input.append(line.strip().split( ))

for direction, amount in puzzle_input:
    amount = int(amount)

    if direction == "U":
        for _ in range(amount):
            header_location[1] += 1
            tail_location = determine_new_tail_location(header_location, tail_location)
            visited_tail_locations.add(tuple(tail_location))
    
    if direction == "D":
        for _ in range(amount):
            header_location[1] -= 1
            tail_location = determine_new_tail_location(header_location, tail_location)
            visited_tail_locations.add(tuple(tail_location))
    
    if direction == "L":
        for _ in range(amount):
            header_location[0] -= 1
            tail_location = determine_new_tail_location(header_location, tail_location)
            visited_tail_locations.add(tuple(tail_location))
    
    if direction == "R":
        for _ in range(amount):
            header_location[0] += 1
            tail_location = determine_new_tail_location(header_location, tail_location)
            visited_tail_locations.add(tuple(tail_location))

print(len(visited_tail_locations))
