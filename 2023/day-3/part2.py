def get_neighbors(coordinates):
    return ((coordinates[0]-1, coordinates[1]), (coordinates[0]-1, coordinates[1]+1), (coordinates[0]-1, coordinates[1]-1), (coordinates[0]+1, coordinates[1]), (coordinates[0]+1, coordinates[1]-1), (coordinates[0]+1, coordinates[1]+1), (coordinates[0], coordinates[1]-1), (coordinates[0], coordinates[1]+1))

running_sum = 0

with open("input.txt", "r") as puzzle_input:
    lines = puzzle_input.readlines()
    numbers = dict()
    symbols = set()
    for line_index, line in enumerate(lines):
        line = line.strip()
        last_number = False
        current_number = ""
        number_coordinates = list()
        for character_index, character in enumerate(line):
            if character == "*":
                symbols.add((line_index, character_index))
            if last_number:
                if character.isdigit():
                    current_number += character
                    number_coordinates.append((line_index, character_index))
                else:
                    if current_number in numbers:
                        numbers[current_number].append(number_coordinates)
                    else:
                        numbers[current_number] = [number_coordinates]
                    number_coordinates = list()
                    current_number = ""
                    last_number = False
            else:
                if character.isdigit():
                    current_number += character
                    number_coordinates.append((line_index, character_index))
                    last_number = True
        if last_number:
            if current_number in numbers:
                numbers[current_number].append(number_coordinates)
            else:
                numbers[current_number] = [number_coordinates]
    
    all_neighbors = set()
    neighbors_to_number = dict()
    for number in numbers:
        for number_coordinates in numbers[number]:
            for number_coordinate in number_coordinates:
                neighbors = get_neighbors(number_coordinate)
                for neighbor in neighbors:
                    all_neighbors.add(neighbor)
                    if number in neighbors_to_number:
                        neighbors_to_number[number].append(neighbor)
                    else:
                        neighbors_to_number[number] = [neighbor]

    for coordinates in symbols:
        mapped_numbers = list()
        if coordinates in all_neighbors:
            for number in neighbors_to_number:
                for coordinate in neighbors_to_number[number]:
                    if coordinate == coordinates:
                        mapped_numbers.append(number)
                        break
        if len(mapped_numbers) == 2:
            product = int(mapped_numbers[0]) * int(mapped_numbers[1])
            running_sum += product

    print(running_sum)