weights_file_name = 'weights.txt'


def get_initial_fuel():
    with open(weights_file_name) as weights_file:
        all_masses = weights_file.readlines()
        total_fuel_required = 0
        for mass in all_masses:
            mass = int(mass)
            total_fuel_required += (mass // 3) - 2
        print(total_fuel_required)
        return total_fuel_required


def get_real_fuel():
    with open(weights_file_name) as weights_file:
        all_masses = weights_file.readlines()
        total_fuel_required = 0
        for mass in all_masses:
            mass = int(mass)
            while mass > 0:
                mass = (mass // 3) - 2
                if mass > 0:
                    total_fuel_required += mass
        print(total_fuel_required)


if __name__ == '__main__':
    get_real_fuel()
