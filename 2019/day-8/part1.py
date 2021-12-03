puzzle_input_list = []

with open("input.txt", "r") as puzzle_input:
    for line in puzzle_input:
        for digit in line:
            puzzle_input_list.append(int(digit))

width = 25
height = 6
digits_per_layer = width*height

layers = [[puzzle_input_list[0]]]

counter = 1
for digit in puzzle_input_list[1:]:
    if counter % digits_per_layer == 0:
        layers.append([digit])
    else:
        layers[-1].append(digit)

    counter += 1

minimum_zeroes = len([digit for digit in layers[0] if digit == 0])
minimum_zeroes_layer = layers[0]

for layer in layers[1:]:
    number_of_zeroes = 0
    for digit in layer:
        if digit == 0:
            number_of_zeroes += 1

    if minimum_zeroes is None:
        minimum_zeroes = number_of_zeroes
        minimum_zeroes_layer = layer
    else:
        if number_of_zeroes < minimum_zeroes:
            minimum_zeroes = number_of_zeroes
            minimum_zeroes_layer = layer

number_of_ones = 0
number_of_twos = 0
for digit in minimum_zeroes_layer:
    if digit == 1:
        number_of_ones += 1
    elif digit == 2:
        number_of_twos += 1
    else:
        pass

print(number_of_ones * number_of_twos)
