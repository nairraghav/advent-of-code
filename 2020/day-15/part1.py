number_and_last_two = {14: [1], 3: [2], 1: [3], 0: [4], 9: [5], 5: [6]}
game_list = [14,3,1,0,9,5]


while len(game_list) < 30000000:
    latest_number = game_list[-1]

    if latest_number not in number_and_last_two or len(number_and_last_two[latest_number]) < 2:
        added_number = 0    
    else:
        added_number = number_and_last_two[latest_number][1] -  number_and_last_two[latest_number][0]

    game_list.append(added_number)
    if added_number in number_and_last_two:
        if len(number_and_last_two[added_number]) == 2:
            number_and_last_two[added_number] = [number_and_last_two[added_number][1], len(game_list)]
        elif len(number_and_last_two[added_number]) == 1:
            number_and_last_two[added_number].append(len(game_list))
    else:   
        number_and_last_two[added_number] = [len(game_list)]


print(game_list[-1])
