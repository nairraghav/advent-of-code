def is_passport_valid(passport_info):
    required_fields = ("byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid")
    
    passport = {}
    passport_fields = passport_info.split(" ")
    for passport_field in passport_fields:
        key, value = passport_field.split(":")
        passport[key] = value

    for required_field in required_fields:
        if required_field not in passport:
            return False

    return True


number_of_valid_passports = 0


with open("input.txt", "r") as puzzle_input:
    current_passport_info = ""
    for line in puzzle_input:
        line = line.strip()
        if len(line) == 0:
            current_passport_info = current_passport_info.strip()

            if is_passport_valid(current_passport_info):
                number_of_valid_passports += 1
            current_passport_info = ""
        else:
            current_passport_info += f" {line}"

    if is_passport_valid(current_passport_info.strip()):
                number_of_valid_passports += 1

print(number_of_valid_passports)
