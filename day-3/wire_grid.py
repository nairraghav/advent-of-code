import sys

wires_file_name = 'wires.txt'


def get_directions():
    with open(wires_file_name) as wires_file:
        first_wire = wires_file.readline()
        second_wire = wires_file.readline()
    return first_wire, second_wire


def get_coordinates_in_wire(wire):
    wire_directions = wire.split(",")
    coordinates_dict = {}
    coordinates_list = []
    current_point = (0, 0)
    for wire_direction in wire_directions:
        direction = wire_direction[0]
        distance = int(wire_direction[1:])
        if direction.upper() == "U":
            for i in range(distance):
                current_point = (current_point[0], current_point[1] + 1)
                coordinates_dict[current_point] = 1
                coordinates_list.append(current_point)
        elif direction.upper() == "D":
            for i in range(distance):
                current_point = (current_point[0], current_point[1] - 1)
                coordinates_dict[current_point] = 1
                coordinates_list.append(current_point)
        elif direction.upper() == "R":
            for i in range(distance):
                current_point = (current_point[0] + 1, current_point[1])
                coordinates_dict[current_point] = 1
                coordinates_list.append(current_point)
        elif direction.upper() == "L":
            for i in range(distance):
                current_point = (current_point[0] - 1, current_point[1])
                coordinates_dict[current_point] = 1
                coordinates_list.append(current_point)
    return coordinates_dict, coordinates_list


def get_common_coordinates(first_wire_coordinates, second_wire_coordinates):
    common_coordinates = []
    for first_coordinate in first_wire_coordinates:
        if first_coordinate in second_wire_coordinates:
            common_coordinates.append(first_coordinate)
    return common_coordinates


def calculate_manhattan_distance(coordinate):
    return abs(coordinate[0]) + abs(coordinate[1])


def get_distances_to_common_coordinates(first_wire_coordinates, second_wire_coordinates, common_coordinates):
    distances = []

    for common_coordinate in common_coordinates:
        first_distance = 0
        second_distance = 0
        for first_wire_coordinate in first_wire_coordinates:
            first_distance += 1
            if common_coordinate == first_wire_coordinate:
                break
        for second_wire_coordinate in second_wire_coordinates:
            second_distance += 1
            if common_coordinate == second_wire_coordinate:
                break
        distances.append(first_distance + second_distance)

    return distances


if __name__ == "__main__":
    first_wire_directions, second_wire_directions = get_directions()
    first_wire_coordinates_dict, first_wire_coordinates_list = get_coordinates_in_wire(first_wire_directions)
    second_wire_coordinates_dict, second_wire_coordinates_list = get_coordinates_in_wire(second_wire_directions)
    common_coordinates = get_common_coordinates(first_wire_coordinates_dict, second_wire_coordinates_dict)
    manhattan_distances = [calculate_manhattan_distance(coordinate) for coordinate in common_coordinates]
    print(manhattan_distances)
    print(min(manhattan_distances))


    distances_to_common_coordinates = get_distances_to_common_coordinates(first_wire_coordinates_list,
                                                                          second_wire_coordinates_list,
                                                                          common_coordinates)
    print(distances_to_common_coordinates)
    print(min(distances_to_common_coordinates))

