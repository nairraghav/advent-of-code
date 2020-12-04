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

    byr = int(passport["byr"])
    if (byr < 1920) or (byr > 2002):
        return False

    iyr = int(passport["iyr"])
    if (iyr < 2010) or (iyr > 2020):
        return False

    eyr = int(passport["eyr"])
    if (eyr < 2020) or (eyr > 2030):
        return False

    if passport["hgt"][-2:] not in ("in", "cm"):
        return False

    hgt = int(passport["hgt"][:-2])
    if passport["hgt"][-2:] == "in":
        if (hgt < 59) or (hgt > 76):
            return False
    else:
        if (hgt < 150) or (hgt > 193):
            return False

    hcl = passport["hcl"]
    if hcl[0] != "#":
        return False

    if len(hcl[1:]) != 6:
        return False

    allowed_alphabets = ("a", "b", "c", "d", "e", "f")
    allowed_numbers = ("0", "1", "2", "3", "4", "5", "6", "7", "8", "9")

    for letter in hcl[1:]:
        if (letter not in allowed_alphabets) and (letter not in allowed_numbers):
            return False

    allowed_eye_colors = ("amb", "blu", "brn", "gry", "grn", "hzl", "oth")
    if passport["ecl"] not in allowed_eye_colors:
        return False

    pid = passport["pid"]
    if len(pid) != 9:
        return False

    for character in pid[3:]:
        if character not in allowed_numbers:
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
