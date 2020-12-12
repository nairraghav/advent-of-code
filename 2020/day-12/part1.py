east_length = 0
north_length = 0

current_direction = "E"

directions_and_angles = {
    "N": {
        "90": "E",
        "180": "S",
        "270": "W"
    },
    "E": {
        "90": "S",
        "180": "W",
        "270": "N"
    },
    "S": {
        "90": "W",
        "180": "N",
        "270": "E"
    },
    "W": {
        "90": "N",
        "180": "E",
        "270": "S"
    }
}
with open("input.txt", "r") as puzzle_input:
    for line in puzzle_input:
        line = line.strip()
        direction = line[0]
        length = line[1:]

        if direction == "R":
            current_direction = directions_and_angles[current_direction][length]
            continue
        elif direction == "L":
            current_direction = directions_and_angles[current_direction][str(360 - int(length))]
            continue
        
        length = int(length)

        if direction == "N":
            north_length += length
        elif direction == "E":
            east_length += length
        elif direction == "S":
            north_length -= length
        elif direction == "W": 
            east_length -= length
        else: # means F
            if current_direction == "N":
                north_length += length
            elif current_direction == "E":
                east_length += length
            elif current_direction == "S":
                north_length -= length
            elif current_direction == "W": 
                east_length -= length


print(abs(east_length) + abs(north_length))
