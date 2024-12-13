def check_all_increasing_or_decreasing(numbers):
    b = [number for number in numbers]
    b.sort()
    c = [number for number in b]
    c.reverse()
    if not (numbers == b or numbers == c):
        return False

    d = {number for number in numbers}
    if len(d) != len(numbers):
        return False
    
    return True




def check_within_range(numbers):
    for index in range(1, len(numbers)):
        if not (1 <= abs(numbers[index] - numbers[index - 1]) <= 3):
            return False
    return True


result = list()
running_sum = 0

with open("input.txt", "r") as puzzle_input:
    lines = puzzle_input.readlines()

    for line in lines:
        line = line.strip()
        numbers = line.split()
        numbers = [int(number) for number in numbers]
        if not check_all_increasing_or_decreasing(numbers):
            result.append("Unsafe1")
            continue

        if not check_within_range(numbers):
            result.append("Unsafe2")
            continue
        result.append("Safe")
        running_sum += 1

    print(result)
    print(running_sum)


