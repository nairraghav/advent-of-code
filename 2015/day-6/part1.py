light_map = []
for _ in range(1000):
    light_map.append([0 for _ in range(1000)])


with open("input.txt", "r") as puzzle_input:
    for line in puzzle_input:
        line = line.split(" ")
        if line[0] == "turn":
            start_x, start_y = line[2].split(",") 
            start_x = int(start_x)
            start_y = int(start_y)
            end_x, end_y = line[4].split(",") 
            end_x = int(end_x)
            end_y = int(end_y)
            turn_on = line[1] == "on"

            for x in range(len(light_map)):
                for y in range(len(light_map[x])):
                    if (x >= start_x and x <= end_x) and (y >= start_y and y <= end_y):
                        if turn_on:
                            light_map[x][y] = 1
                        else:
                            light_map[x][y] = 0
        elif line[0] == "toggle":
            start_x, start_y = line[1].split(",") 
            start_x = int(start_x)
            start_y = int(start_y)
            end_x, end_y = line[3].split(",") 
            end_x = int(end_x)
            end_y = int(end_y)

            for x in range(len(light_map)):
                for y in range(len(light_map[x])):
                    if (x >= start_x and x <= end_x) and (y >= start_y and y <= end_y):
                        if light_map[x][y] == 0:
                            light_map[x][y] = 1
                        else:
                            light_map[x][y] = 0
        else:
            raise ValueError("Invalid Operation")

lights_lit = 0
for x in range(len(light_map)):
    for y in range(len(light_map[x])):
        if light_map[x][y] == 1:
            lights_lit += 1

print(lights_lit)