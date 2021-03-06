def is_int(int_string):
    try:
        int(int_string)
        return True
    except:
        return False


def calculate(first_number, second_number, operation):
    if operation == "+":
        return first_number + second_number
    elif operation == "*":
        return first_number * second_number


def simplify(input_string):
    first_number = None
    second_number = None
    operation = None
    input_string = input_string.split()
    for character in input_string:
        if is_int(character):
            if first_number is None:
                first_number = int(character)
            elif second_number is None:
                second_number = int(character)
        else:
            operation = character

        if first_number is not None and second_number is not None:
            first_number = calculate(first_number, second_number, operation)
            operation = None
            second_number = None
    return first_number

running_total = 0
with open("input.txt", "r") as puzzle_input:
    for line in puzzle_input:
        line = line.strip()
        while "(" in line or ")" in line:
            starting_index = None
            ending_index = None
            for index in range(len(line)):
                if line[index] == "(":
                    starting_index = index
                elif line[index] == ")":
                    ending_index = index
                    break
            result = simplify(line[starting_index+1:ending_index])
            line = line[:starting_index] + str(result) + line[ending_index+1:]

        running_total += simplify(line)

print(running_total)
