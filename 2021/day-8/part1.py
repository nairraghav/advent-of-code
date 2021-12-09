puzzle_input_list = []

with open("input.txt", "r") as puzzle_input:
    for line in puzzle_input:
        line = line.strip()
        input_string, output_string = line.split(" | ")
        output = output_string.split()
        puzzle_input_list.append(output)

lengths_we_care_about = {2, 4, 3, 7}
number_of_appearances = 0

for outputs in puzzle_input_list:
    for output in outputs:
        if len(output) in lengths_we_care_about:
            number_of_appearances += 1

print(number_of_appearances)
