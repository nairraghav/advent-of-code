east_length = 0
north_length = 0
waypoint = [10, 1] # east, north

with open("input.txt", "r") as puzzle_input:
    for line in puzzle_input:
        line = line.strip()
        direction = line[0]
        length = int(line[1:])

        if direction == "N":
            waypoint[1] += length
        elif direction == "S":
            waypoint[1] -= length
        elif direction == "E":
            waypoint[0] += length
        elif direction == "W":
            waypoint[0] -= length
        elif direction == "L":
            if length == 90:
                waypoint = [-1 * waypoint[1], waypoint[0]]
            elif length == 180:
                waypoint = [-1 * waypoint[0], -1 * waypoint[1]]
            elif length == 270:
                waypoint = [waypoint[1], -1 * waypoint[0]]
        elif direction == "R":
            if length == 90:
                waypoint = [waypoint[1], -1 * waypoint[0]]
            elif length == 180:
                waypoint = [-1 * waypoint[0], -1 * waypoint[1]]
            elif length == 270:
                waypoint = [-1 * waypoint[1], waypoint[0]]
        else: # Forward
            east_length += length * waypoint[0]
            north_length += length * waypoint[1]

        #print(waypoint)
        #print(east_length, north_length)

print(abs(east_length) + abs(north_length))


"""
10, 4

4, -10

-10, -4

-4, 10

10, 4
"""