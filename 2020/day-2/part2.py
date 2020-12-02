good_passwords = 0
with open("input.txt", "r") as puzzle_input:
    for line in puzzle_input:
        first_last, letter_colon, password = line.split(" ")
        first_index, last_index = first_last.split("-")
        first_index = int(first_index) - 1
        last_index = int(last_index) - 1
        letter = letter_colon[0]
        
        if password[first_index] != password[last_index]:
            if (password[first_index] == letter) or (password[last_index] == letter):
                good_passwords += 1

print(f"Number of good passwords: {good_passwords}")
