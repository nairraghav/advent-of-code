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

def check_all_keys_at_z(current_keys):
    for key in current_keys:
        if key[-1] != "Z":
            return False
    
    return True

def main():
    lines = get_input()
    pathing = lines[0]
    mapping = get_mapping(lines[1:])

    current_keys = list()
    for map_key in mapping:
        if map_key[-1] == "A":
            current_keys.append(map_key) 
    
    lcm_numbers = list()
    for current_key_index in range(len(current_keys)):
        current_pathing_index = 0
        total_steps = 0
        first_and_second_steps = list()
        while current_keys[current_key_index][-1] != "Z":
            if pathing[current_pathing_index] == "L":
                current_keys[current_key_index] = mapping[current_keys[current_key_index]][0]
            else:
                current_keys[current_key_index] = mapping[current_keys[current_key_index]][1]
        
            current_pathing_index += 1
            current_pathing_index %= len(pathing)
            total_steps += 1

            first_and_second_steps.append(total_steps)

        lcm_numbers.append(total_steps)
    
    import math
    print(math.lcm(*lcm_numbers))

if __name__ == "__main__":
    main()