
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
    length_of_adjacent_numbers = 1
    contains_same_adjacent_digits = False
    contains_multiple_adjacent_only = False
    for index in range(len(num_string) - 1):
        if num_string[index] > num_string[index + 1]:
            return False
        if num_string[index] == num_string[index + 1]:
            length_of_adjacent_numbers += 1
        else:
            if not contains_same_adjacent_digits and length_of_adjacent_numbers > 2:
                contains_multiple_adjacent_only = True
            if length_of_adjacent_numbers == 2:
                contains_multiple_adjacent_only = False
            if length_of_adjacent_numbers > 1:
                contains_same_adjacent_digits = True
            length_of_adjacent_numbers = 1
    if not contains_same_adjacent_digits and length_of_adjacent_numbers > 2:
        contains_multiple_adjacent_only = True
    if length_of_adjacent_numbers == 2:
        contains_multiple_adjacent_only = False
    if contains_multiple_adjacent_only:
        return False
    if not contains_same_adjacent_digits:
        return False
    return True


def get_potential_passwords():
    potential_passwords = []
    for password_guess in range(low_range, high_range):
        if check_if_number_fits_initial_requirements(str(password_guess)):
        # if check_if_number_fits_updated_requirements(str(password_guess)):
            potential_passwords.append(password_guess)
    return potential_passwords



if __name__ == "__main__":
    potential_passwords = get_potential_passwords()
    # print(potential_passwords)
    # print(len(potential_passwords))
    bad_passwords = []
    for password in potential_passwords:
        if not check_if_number_fits_updated_requirements(str(password)):
            bad_passwords.append(password)
    print(bad_passwords)
    print(len(bad_passwords))