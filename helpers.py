def get_all_neighbors(coordinates):
    return ((coordinates[0]-1, coordinates[1]), (coordinates[0]-1, coordinates[1]+1), (coordinates[0]-1, coordinates[1]-1), (coordinates[0]+1, coordinates[1]), (coordinates[0]+1, coordinates[1]-1), (coordinates[0]+1, coordinates[1]+1), (coordinates[0], coordinates[1]-1), (coordinates[0], coordinates[1]+1))

def get_horizontal_vertical_neighbors(coordinates):
    return ((coordinates[0]-1, coordinates[1]), (coordinates[0]+1, coordinates[1]), (coordinates[0], coordinates[1]-1), (coordinates[0], coordinates[1]+1))