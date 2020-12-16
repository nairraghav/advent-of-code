number_and_last_two = {14: [1], 3: [2], 1: [3], 0: [4], 9: [5], 5: [6]}
game_list = [14,3,1,0,9,5]


index = len(game_list) + 1
latest_number = game_list[-1]
while index <= 30000000:
    if latest_number not in number_and_last_two or len(number_and_last_two[latest_number]) < 2:
        added_number = 0    
    else:
        added_number = number_and_last_two[latest_number][1] -  number_and_last_two[latest_number][0]

    if added_number in number_and_last_two:
        if len(number_and_last_two[added_number]) == 2:
            number_and_last_two[added_number] = [number_and_last_two[added_number][1], index]
        elif len(number_and_last_two[added_number]) == 1:
            number_and_last_two[added_number].append(index)
    else:   
        number_and_last_two[added_number] = [index]
    latest_number = added_number
    index += 1


print(latest_number)
