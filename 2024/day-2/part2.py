def check_all_increasing(numbers, allowed_single_failure):
    b = [number for number in numbers]
    index = 1
    while index < len(b):
        if b[index] <= b[index-1]:
            if allowed_single_failure:
                return False, b
            else:
                allowed_single_failure = True
                del b[index]
                index -= 1  # offset
        index += 1
    return True, b


def check_all_decreasing(numbers, allowed_single_failure):
    b = [number for number in numbers]
    index = 1
    while index < len(b):
        if b[index] >= b[index-1]:
            if allowed_single_failure:
                return False, b
            else:
                allowed_single_failure = True
                del b[index]
                index -= 1  # offset
        index += 1            
    return True, b


def check_all_increasing_or_decreasing(numbers, allowed_single_failure=False):
    a, b = check_all_increasing(numbers, allowed_single_failure=allowed_single_failure)
    print(a)
    if a:
        numbers = b
        return True

    c, d = check_all_decreasing(numbers, allowed_single_failure=allowed_single_failure)
    print (c)
    if c:
        numbers = d
        return True
        
    return False


def check_within_range(numbers):
    b = [number for number in numbers]
    allowed_single_failure = False
    index = 1
    while index < len(b):
        if not (1 <= abs(b[index] - b[index - 1]) <= 3):
            if allowed_single_failure:
                return False, b
            else:
                allowed_single_failure = True
                del b[index]
                index -= 1  # offset
        index += 1
    return True, b


result = list()
running_sum = 0

with open("input.txt", "r") as puzzle_input:
    lines = puzzle_input.readlines()

    for line in lines:
        line = line.strip()
        numbers = line.split()
        numbers = [int(number) for number in numbers]
        print(numbers)
        if not check_all_increasing_or_decreasing(numbers):
            result.append("Unsafe1")
            continue

        a, b = check_within_range(numbers)
        if not a:
            result.append("Unsafe2")
            continue

        result.append("Safe")
        running_sum += 1

    print(result)
    print(running_sum)
