seat_map = []

with open("input.txt", "r") as puzzle_input:
    for line in puzzle_input:
        seat_map.append([l for l in line.strip()])



rounds = 1
has_changed = True
while has_changed:
    has_changed = False
    new_seat_map = []
    for x in range(len(seat_map)):
        row = []
        for y in range(len(seat_map[x])):
            eight_values = [(x-1, y-1), (x, y-1), (x+1, y-1),
                            (x-1, y),             (x+1, y),
                            (x-1, y+1), (x, y+1), (x+1, y+1)]

            occupied_nearby_seats = 0
            for check_x, check_y in eight_values:
                if (0 <= check_x < len(seat_map)) and (0 <= check_y < len(seat_map[x])):
                    if seat_map[check_x][check_y] == "#":
                        occupied_nearby_seats += 1

            if (seat_map[x][y] == "L") and (occupied_nearby_seats == 0):
                has_changed = True
                row.append("#")
            elif (seat_map[x][y] == "#") and (occupied_nearby_seats >= 4):
                row.append("L")
                has_changed = True
            else:
                row.append(seat_map[x][y])
        new_seat_map.append(row)
    seat_map = new_seat_map
    rounds += 1

occupied_seats = 0
for x in range(len(seat_map)):
    for y in range(len(seat_map[x])):
        if seat_map[x][y] == "#":
            occupied_seats += 1

print("occupied seats", occupied_seats)
