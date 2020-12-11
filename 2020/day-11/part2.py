import pprint

seat_map = []

with open("input.txt", "r") as puzzle_input:
    for line in puzzle_input:
        seat_map.append([l for l in line.strip()])


rounds = 0
has_changed = True
while has_changed:
    rounds += 1
    print(rounds)
    has_changed = False
    new_seat_map = []
    for x in range(len(seat_map)):
        row = []
        for y in range(len(seat_map[x])):
            occupied_nearby_seats = 0

            range_x = list(range(x))
            range_x.reverse()

            for check_x in range_x:
                if seat_map[check_x][y] == "#":
                    occupied_nearby_seats += 1
                    break
                elif seat_map[check_x][y] == "L":
                    break

            for check_x in range(x+1, len(seat_map)):
                if seat_map[check_x][y] == "#":
                    occupied_nearby_seats += 1
                    break
                elif seat_map[check_x][y] == "L":
                    break

            range_y = list(range(y))
            range_y.reverse()
            for check_y in range_y:
                if seat_map[x][check_y] == "#":
                    occupied_nearby_seats += 1
                    break
                elif seat_map[x][check_y] == "L":
                    break

            for check_y in range(y+1, len(seat_map[x])):
                if seat_map[x][check_y] == "#":
                    occupied_nearby_seats += 1
                    break
                elif seat_map[x][check_y] == "L":
                    break

            check_x = x - 1
            check_y = y - 1
            while (check_x >= 0) and (check_y >= 0):
                if seat_map[check_x][check_y] == "#":
                    occupied_nearby_seats += 1
                    break
                elif seat_map[check_x][check_y] == "L":
                    break
                check_x -= 1
                check_y -= 1

            check_x = x - 1
            check_y = y + 1
            while (check_x >= 0) and (check_y < len(seat_map[x])):
                if seat_map[check_x][check_y] == "#":
                    occupied_nearby_seats += 1
                    break
                elif seat_map[check_x][check_y] == "L":
                    break
                check_x -= 1
                check_y += 1

            check_x = x + 1
            check_y = y - 1
            while (check_y >= 0) and (check_x < len(seat_map)):
                if seat_map[check_x][check_y] == "#":
                    occupied_nearby_seats += 1
                    break
                elif seat_map[check_x][check_y] == "L":
                    break
                check_x += 1
                check_y -= 1

            check_x = x + 1
            check_y = y + 1
            while (check_y < len(seat_map[x])) and (check_x < len(seat_map)):
                if seat_map[check_x][check_y] == "#":
                    occupied_nearby_seats += 1
                    break
                elif seat_map[check_x][check_y] == "L":
                    break
                check_x += 1
                check_y += 1

            if (seat_map[x][y] == "L") and (occupied_nearby_seats == 0):
                has_changed = True
                row.append("#")
            elif (seat_map[x][y] == "#") and (occupied_nearby_seats >= 5):
                row.append("L")
                has_changed = True
            else:
                row.append(seat_map[x][y])
        new_seat_map.append(row)
    seat_map = new_seat_map

occupied_seats = 0
for x in range(len(seat_map)):
    for y in range(len(seat_map[x])):
        if seat_map[x][y] == "#":
            occupied_seats += 1

print("occupied seats", occupied_seats)
