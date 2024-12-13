from pprint import pprint
from copy import deepcopy


def get_lines_from_input_stripped():
    output = list()
    with open("input.txt", "r") as puzzle_input:
        lines = puzzle_input.readlines()
        for line in lines:
            line = line.strip()
            total, operators = line.split(": ")
            total = int(total)
            operators = operators.split(" ")
            operators = [int(operator) for operator in operators]
            if line:
                output.append((total, operators))
    return output


def recursive_check(current_sum, expected_total, operators):
    if current_sum == expected_total:
        return True

    if current_sum > expected_total:
        return False

    if not operators:
        return False
    
    operator = operators[0]
    operators_a = operators[1:]#deepcopy(operators)
    operators_b = operators[1:]#deepcopy(operators)
    operators_c = operators[1:]#deepcopy(operators)
    return recursive_check(current_sum*operator, expected_total, operators_a) or recursive_check(current_sum+operator, expected_total, operators_b) or recursive_check(int(f"{current_sum}{operator}"), expected_total, operators_c)


def main():
    output = get_lines_from_input_stripped()
    pprint(output)

    running_sum = 0
    running_iterator = 0
    for total, operators in output:
        print(running_iterator)
        running_iterator += 1
        if recursive_check(0, total, operators):
            running_sum += total
            print(total, operators)
    print(running_sum)


if __name__ == "__main__":
    main()
