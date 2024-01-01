def get_input():
    puzzle_lines = list()
    with open("input.txt", "r") as puzzle_input:
        lines = puzzle_input.readlines()
        for line in lines[0].split(","):
            line = line.strip()
            puzzle_lines.append(line)
    
    return puzzle_lines

def get_hash(line):
    running_sum = 0
    for character in line:
        running_sum += ord(character)
        running_sum *= 17
        running_sum %= 256

    print(running_sum)
    return running_sum

def main():
    lines = get_input()
    running_sum = 0
    for line in lines:
        running_sum += get_hash(line)

    print(running_sum)


if __name__ == "__main__":
    main()