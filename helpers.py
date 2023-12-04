def get_all_neighbors(coordinates):
    return ((coordinates[0]-1, coordinates[1]), (coordinates[0]-1, coordinates[1]+1), (coordinates[0]-1, coordinates[1]-1), (coordinates[0]+1, coordinates[1]), (coordinates[0]+1, coordinates[1]-1), (coordinates[0]+1, coordinates[1]+1), (coordinates[0], coordinates[1]-1), (coordinates[0], coordinates[1]+1))

def get_horizontal_vertical_neighbors(coordinates):
    return ((coordinates[0]-1, coordinates[1]), (coordinates[0]+1, coordinates[1]), (coordinates[0], coordinates[1]-1), (coordinates[0], coordinates[1]+1))

def get_lines_from_input_stripped():
    output_lines = list()
    with open("input.txt", "r") as puzzle_input:
        lines = puzzle_input.readlines()
        for line_index, line in enumerate(lines):
            output_lines.append(line.strip())
    return output_lines
        