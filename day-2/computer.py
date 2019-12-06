intcode_file_name = 'intcode.txt'


def intcode_add(intcode, index):
    intcode[intcode[index + 3]] = intcode[intcode[index + 1]] + intcode[intcode[index + 2]]
    return intcode


def intcode_multiply(intcode, index):
    intcode[intcode[index + 3]] = intcode[intcode[index + 1]] * intcode[intcode[index + 2]]
    return intcode


def intcode_program():
    with open(intcode_file_name) as intcode_file:
        intcode = intcode_file.readline()
        intcode = intcode.split(',')
        intcode = [int(number) for number in intcode]
        index = 0
        while intcode[index] != 99:
            if intcode[index] == 1:
                intcode = intcode_add(intcode, index)
            elif intcode[index] == 2:
                intcode = intcode_multiply(intcode, index)
            index += 4
        print(intcode)
        return intcode


if __name__ == "__main__":
    intcode_program()
