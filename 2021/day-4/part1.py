def won_bingo(bingo_card):
    # check all the rows
    for row in range(len(bingo_card)):
        horizontal_count = 0
        vertical_count = 0
        for col in range(len(bingo_card[row])):
            if bingo_card[col][row] == -1:
                vertical_count += 1
            if bingo_card[row][col] == -1:
                horizontal_count += 1
        if (horizontal_count == 5) or (vertical_count == 5):
            return True

    # no match found
    return False

bingo_cards = []
bingo_numbers = []

with open("input.txt", "r") as puzzle_input:
    
    index = 0
    for line in puzzle_input:
        line = line.strip()
        if index == 0:
            bingo_numbers = [int(number) for number in line.split(",")]
            index += 1
            bingo_card = []
            continue
        
        if (index > 0) and (line):
            bingo_line = [int(number) for number in line.split()]
            bingo_card.append(bingo_line)
            # starting or still in bingo card
        else:
            bingo_cards.append(bingo_card)
            bingo_card = []# space between bingo cards
bingo_cards.append(bingo_card)
del bingo_cards[0]

print(bingo_numbers)
print(bingo_cards)

game_over = False
last_number_called = None
bingo_card_winner = None
for bingo_number in bingo_numbers:
    if game_over is True:
        break
    
    for bingo_card in bingo_cards:
        found_number = False
        for row in range(len(bingo_card)):
            if found_number is True:
                break
            for col in range(len(bingo_card[row])):
                if bingo_card[row][col] == bingo_number:
                    bingo_card[row][col] = -1
                    found_number = True
                    break
        if won_bingo(bingo_card):
            bingo_card_winner = bingo_card
            last_number_called = bingo_number
            game_over = True
            break

remaining_sum = 0
for row in range(len(bingo_card_winner)):
    for col in range(len(bingo_card_winner[row])):
        if bingo_card_winner[row][col] != -1:
            remaining_sum += bingo_card_winner[row][col]

print(bingo_card_winner)
print(last_number_called)
print(remaining_sum)
print(remaining_sum * last_number_called)