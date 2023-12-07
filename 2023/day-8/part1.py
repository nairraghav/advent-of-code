def get_input():
    puzzle_lines = list()
    with open("input.txt", "r") as puzzle_input:
        lines = puzzle_input.readlines()
        for line in lines:
            line = line.strip()
            if line:
                puzzle_lines.append()
    
    return puzzle_lines


def main():
    lines = get_input()


if __name__ == "__main__":
    main()