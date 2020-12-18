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


def simplify_first(input_string):
    while "+" in input_string:
        starting_index = None
        ending_index = None
        for index in range(len(input_string)):
            if input_string[index] == "+":
                starting_subset = input_string[:index-2]
                starting_index = starting_subset.rfind(" ")
                if starting_index < 0:
                    starting_index = 0
                else:
                    starting_index += 1
                ending_subset = input_string[index+2:]
                ending_index = ending_subset.find(" ") - 1
                if ending_index < 0:
                    ending_index = len(ending_subset)

                ending_index += index + 2
        
        result = simplify(input_string[starting_index:ending_index+1])
        input_string = input_string[:starting_index] + str(result) + input_string[ending_index+1:]

    return simplify(input_string)

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
            result = simplify_first(line[starting_index+1:ending_index])
            line = line[:starting_index] + str(result) + line[ending_index+1:]
            print(line)
        running_total += simplify_first(line)

print(running_total)
