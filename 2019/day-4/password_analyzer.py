
low_range = 158126
high_range = 624574


def check_if_number_fits_initial_requirements(num_string):
    contains_same_adjacent_digits = False
    for index in range(len(num_string) - 1):
        if num_string[index] > num_string[index + 1]:
            return False
        if num_string[index] == num_string[index + 1]:
            contains_same_adjacent_digits = True
    if not contains_same_adjacent_digits:
        return False
    return True


def check_if_number_fits_updated_requirements(num_string):
    for character_in_num_string in num_string:
        if num_string.count(character_in_num_string) == 2:
            return True


def get_potential_passwords():
    potential_passwords = []
    for password_guess in range(low_range, high_range):
        if check_if_number_fits_initial_requirements(str(password_guess)):
            potential_passwords.append(password_guess)
    return potential_passwords


if __name__ == "__main__":
    potential_passwords = get_potential_passwords()
    print(potential_passwords)
    print(len(potential_passwords))

    new_potential_passwords = []
    for password in potential_passwords:
        if check_if_number_fits_updated_requirements(str(password)):
            new_potential_passwords.append(password)
    print(new_potential_passwords)
    print(len(new_potential_passwords))