from copy import deepcopy


def check_all_increasing(numbers):
    b = [number for number in numbers]
    index = 1
    while index < len(b):
        if b[index] <= b[index-1]:
            return False
        index += 1
    return True


def check_all_decreasing(numbers):
    b = [number for number in numbers]
    index = 1
    while index < len(b):
        if b[index] >= b[index-1]:
            return False
        index += 1            
    return True


def check_all_increasing_or_decreasing(numbers):
    if check_all_increasing(numbers):
        return True

    if check_all_decreasing(numbers):
        return True

    return False


def check_within_range(numbers):
    b = [number for number in numbers]
    index = 1
    while index < len(b):
        if not (1 <= abs(b[index] - b[index - 1]) <= 3):
            return False
        index += 1
    return True


result = list()
running_sum = 0

with open("input.txt", "r") as puzzle_input:
    lines = puzzle_input.readlines()

    for line in lines:
        line = line.strip()
        numbers = line.split()
        numbers = [int(number) for number in numbers]
        if check_all_increasing_or_decreasing(numbers) and check_within_range(numbers):
            running_sum += 1
            result.append(numbers)
            continue

        for index_to_remove in range(len(numbers)):
            new_numbers = deepcopy(numbers)
            new_numbers.pop(index_to_remove)
            if check_all_increasing_or_decreasing(new_numbers) and check_within_range(new_numbers):
                running_sum += 1
                result.append(new_numbers)
                break
    
    print(result)
    print(running_sum)
