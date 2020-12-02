def get_word_dict(word: str) -> dict:
    word_dict = {}
    for letter in word:
        if letter in word_dict:
            word_dict[letter] += 1
        else:
            word_dict[letter] = 1
    return word_dict

good_passwords = 0
with open("input.txt", "r") as puzzle_input:
    for line in puzzle_input:
        min_max, letter_colon, password = line.split(" ")
        minimum, maximum = min_max.split("-")
        minimum = int(minimum)
        maximum = int(maximum)
        letter = letter_colon[0]
        word_dict = get_word_dict(password)
        if letter in word_dict:
            if minimum <= word_dict[letter] <= maximum:
                good_passwords += 1

print(f"Number of good passwords: {good_passwords}")

