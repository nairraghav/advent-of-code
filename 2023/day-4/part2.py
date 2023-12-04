def get_lines_from_input_stripped():
    output_lines = list()
    with open("input.txt", "r") as puzzle_input:
        lines = puzzle_input.readlines()
        for line in lines:
            all_numbers = line.split(":")[-1]
            all_numbers = all_numbers.strip()
            winning_numbers, have_numbers = all_numbers.split("|")
            winning_numbers = winning_numbers.strip()
            have_numbers = have_numbers.strip()
            winning_numbers = {int(number) for number in winning_numbers.split()}
            have_numbers = [int(number) for number in have_numbers.split()]
            output_lines.append((winning_numbers, have_numbers))
        
    return output_lines


def main():
    lines = get_lines_from_input_stripped()
    card_counts = {line_count+1: 1 for line_count, _ in enumerate(lines)}
    for card_number, line in enumerate(lines):
        card_number += 1
        winning_numbers, have_numbers = line
        number_matches = 0
        for number in have_numbers:
            if number in winning_numbers:
                number_matches += 1
        if number_matches > 0:
            for won_card_to_add in range(1, number_matches+1):
                if (card_number + won_card_to_add) not in card_counts:
                    break
                card_counts[card_number+won_card_to_add] += 1 * card_counts[card_number]
    print(sum(card_counts.values()))


if __name__ == "__main__":
    main()


{1: 1, }