def get_input():
    puzzle_lines = list()
    with open("input.txt", "r") as puzzle_input:
        lines = puzzle_input.readlines()
        for line in lines:
            line = line.strip()
            if line:
                puzzle_lines.append(line)
    
    return puzzle_lines

def get_mapping(lines):
    mapping = dict()
    for line in lines:
        key, values = line.split("=")
        key = key.strip()
        values = values.strip()
        left_value, right_value = values.strip("(").strip(")").split(", ")
        mapping[key] = (left_value, right_value)
    return mapping

def main():
    lines = get_input()
    pathing = lines[0]
    mapping = get_mapping(lines[1:])

    current_key = "AAA"
    current_pathing_index = 0
    goal = "ZZZ"
    total_steps = 0

    while current_key != goal:
        if pathing[current_pathing_index] == "L":
            current_key = mapping[current_key][0]
        else:
            current_key = mapping[current_key][1]
        
        current_pathing_index += 1
        current_pathing_index %= len(pathing)

        total_steps += 1
    
    print(total_steps)


if __name__ == "__main__":
    main()