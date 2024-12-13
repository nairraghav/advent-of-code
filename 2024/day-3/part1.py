import re
running_sum = 0

with open("input.txt", "r") as puzzle_input:
    lines = puzzle_input.readlines()

    for line in lines:
        matches = re.findall("mul\([0-9]{1,3},[0-9]{1,3}\)", line)
        for match in matches:
            match = match[4:-1]
            match = match.split(",")
            running_sum += int(match[0]) * int(match[1])
    
print(running_sum)