puzzle_input_list = []

with open("input.txt", "r") as puzzle_input:
    for line in puzzle_input:
        line = line.strip()
        start, end = line.split(" -> ")
        start_x, start_y = start.split(",")
        start_x = int(start_x)
        start_y = int(start_y)
        end_x, end_y = end.split(",")
        end_x = int(end_x)
        end_y = int(end_y)
        puzzle_input_list.append([(start_x, start_y), (end_x, end_y)])


coordinates = dict()

for start, end in puzzle_input_list:
    #print(start, end)
    start_x = start[0]
    start_y = start[1]
    end_x = end[0]
    end_y = end[1]

    if (end_y - start_y == 0):  # horizontal line
        min_x = min(start_x, end_x)
        max_x = max(start_x, end_x)
        for difference in range(max_x - min_x + 1):
            coordinates[(min_x+difference, start_y)] = coordinates.get((min_x+difference, start_y), 0) + 1
    elif (end_x - start_x == 0):  # vertical line
        min_y = min(start_y, end_y)
        max_y = max(start_y, end_y)
        for difference in range(max_y - min_y + 1):
            coordinates[(start_x, min_y+difference)] = coordinates.get((start_x, min_y+difference), 0) + 1
    elif (abs(end_y - start_y) == abs(end_x - start_x)):  # diagonal line
        print((start_x, start_y), (end_x, end_y))
        if (start_x < end_x) and (start_y < end_y):
            for difference in range(end_x - start_x + 1):
                print((start_x+difference, start_y+difference))
                coordinates[(start_x+difference, start_y+difference)] = coordinates.get((start_x+difference, start_y+difference), 0) + 1
        elif (start_x < end_x) and (start_y > end_y):
            for difference in range(end_x - start_x + 1):
                print((start_x+difference, start_y-difference))
                coordinates[(start_x+difference, start_y-difference)] = coordinates.get((start_x+difference, start_y-difference), 0) + 1
        elif (start_x > end_x) and (start_y > end_y):
            for difference in range(start_x - end_x + 1):
                print((start_x-difference, start_y-difference))
                coordinates[(start_x-difference, start_y-difference)] = coordinates.get((start_x-difference, start_y-difference), 0) + 1
        elif (start_x > end_x) and (start_y < end_y):
            for difference in range(start_x - end_x + 1):
                print((start_x-difference, start_y+difference))
                coordinates[(start_x-difference, start_y+difference)] = coordinates.get((start_x-difference, start_y+difference), 0) + 1        
        else:  # invalid diagonal case
            pass
    else:  # we don't care
        pass

count_of_more_than_two = 0
for coordinate in coordinates:
    if coordinates[coordinate] >= 2:
        count_of_more_than_two += 1

print(count_of_more_than_two)