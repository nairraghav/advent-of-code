puzzle_input_list = []

with open("input.txt", "r") as puzzle_input:
    for line in puzzle_input:
        line = line.strip()
        puzzle_input_list.append(line)

gamma = ""
epsilon = ""

count_of_digits = [{0: 0, 1: 0} for _ in range(len(puzzle_input_list[0]))]

for binary_string in puzzle_input_list:
    index = 0
    for character in binary_string:
        if character == "0":
            count_of_digits[index][0] += 1
        else:
            count_of_digits[index][1] += 1
        index += 1

for digit_counter in count_of_digits:
    if digit_counter[0] > digit_counter[1]:
        gamma += "0"
        epsilon += "1"
    else:
        gamma += "1"
        epsilon += "0"

print(gamma)
print(epsilon)

# used binary calculator to determine final answer
# 4139586