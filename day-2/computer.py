intcode_file_name = 'intcode.txt'


def intcode_add(intcode, index):
    intcode[intcode[index + 3]] = intcode[intcode[index + 1]] + intcode[intcode[index + 2]]
    return intcode


def intcode_multiply(intcode, index):
    intcode[intcode[index + 3]] = intcode[intcode[index + 1]] * intcode[intcode[index + 2]]
    return intcode


def get_intcode_input():
    intcode = None
    with open(intcode_file_name) as intcode_file:
        intcode = intcode_file.readline()
        intcode = intcode.split(',')
        intcode = [int(number) for number in intcode]
    if intcode:
        return intcode
    else:
        raise NotImplementedError('Intcode is None')


def intcode_program(intcode):
    index = 0
    while intcode[index] != 99:
        if intcode[index] == 1:
            intcode = intcode_add(intcode, index)
        elif intcode[index] == 2:
            intcode = intcode_multiply(intcode, index)
        index += 4
    print(intcode)
    return intcode


def find_noun_verb():
    expected_output = 19690720
    for noun in range(99):
        for verb in range(99):
            intcode = get_intcode_input()
            print(f"Default Intcode Start: {intcode[0]}")
            intcode[1] = noun
            intcode[2] = verb
            if intcode_program(intcode)[0] == expected_output:
                return noun, verb
    return "No Valid Combination"


if __name__ == "__main__":
    # intcode_input = get_intcode_input()
    # intcode_program(intcode_input)
    find_noun_verb()