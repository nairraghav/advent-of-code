def get_lines_from_input_stripped():
    order_lines = list()
    sequence_lines = list()
    order_lines_section = True
    with open("input.txt", "r") as puzzle_input:
        lines = puzzle_input.readlines()
        for line in lines:
            line = line.strip()
            if line:
                if order_lines_section:
                    order_lines.append(line)
                else:
                    sequence_lines.append(line)
            else:
                order_lines_section = False
    order_lines = [order_line.split("|") for order_line in order_lines]
    sequence_lines = [sequence_line.split(",") for sequence_line in sequence_lines]
    return order_lines, sequence_lines


def is_before(before, after, order):
    if before not in order:
        return False

    return after in order[before]


def fix_sequence(sequence, order):
    for sequence_line_index in range(len(sequence) - 1):
            if not is_before(sequence[sequence_line_index], sequence[sequence_line_index + 1], order):
                print(sequence)
                sequence[sequence_line_index], sequence[sequence_line_index + 1] = sequence[sequence_line_index + 1], sequence[sequence_line_index]
                print(sequence)
                return fix_sequence(sequence, order)
    return sequence


def main():
    running_sum = 0
    order = dict()
    order_lines, sequence_lines = get_lines_from_input_stripped()
    for previous, after in order_lines:
        previous = int(previous)
        after = int(after)
        if previous in order:
            order[previous].append(after)
        else:
            order[previous] = [after]

    sequence_lines = [[int(sequence) for sequence in sequence_line] for sequence_line in sequence_lines]
    failed_sequences = list()
    for sequence_line in sequence_lines:
        failed = False
        for sequence_line_index in range(len(sequence_line) - 1):
            if not is_before(sequence_line[sequence_line_index], sequence_line[sequence_line_index + 1], order):
                failed = True
                failed_sequences.append(sequence_line)                
                break

    
    for failed_sequence in failed_sequences:
        failed_sequence = fix_sequence(failed_sequence, order)
        running_sum += failed_sequence[len(failed_sequence) // 2]

    print(running_sum)

if __name__ == "__main__":
    main()
