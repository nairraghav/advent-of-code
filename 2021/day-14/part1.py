puzzle_input_list = []

with open("input.txt", "r") as puzzle_input:
    for line in puzzle_input:
        line = line.strip()
        puzzle_input_list.append(line)

del puzzle_input_list[1]

input_string = puzzle_input_list[0]
insertion_rules = dict()

for insertion_rule in puzzle_input_list[1:]:
    insertion_input, insertion_output = insertion_rule.split(" -> ")
    insertion_rules[insertion_input] = insertion_output

final_string = input_string[0]

for _ in range(10):
    final_string = input_string[0]
    for string_index in range(len(input_string)-1):
        insertion_key = input_string[string_index:string_index+2]
        insert = insertion_rules.get(insertion_key)
        final_string += f"{insert}{insertion_key[-1]}"
    input_string = final_string

print(input_string)

frequency = dict()
max_frequency = None
min_frequency = None
for character in input_string:
    frequency[character] = frequency.get(character, 0) + 1

for frequency_key in frequency:
    if max_frequency is None:
        max_frequency = frequency[frequency_key]
    else:
        max_frequency = max(max_frequency, frequency[frequency_key])
    
    if min_frequency is None:
        min_frequency = frequency[frequency_key]
    else:
        min_frequency = min(min_frequency, frequency[frequency_key])

print(max_frequency - min_frequency)