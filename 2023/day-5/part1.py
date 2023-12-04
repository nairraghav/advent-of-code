def get_lines_from_input_stripped():
    output_lines = list()
    with open("input.txt", "r") as puzzle_input:
        lines = puzzle_input.readlines()
        for line in lines:
            output_lines.append(line.strip())
        
    return output_lines

def main():
    running_sum = 0
    lines = get_lines_from_input_stripped()
    
    print(running_sum)

if __name__ == "__main__":
    main()