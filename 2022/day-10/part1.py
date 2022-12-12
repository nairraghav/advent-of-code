puzzle_input = list()
cycle = 1
important_cycles = {20, 60, 100, 140, 180, 220}
x_value = 1
result = list()


with open("input.txt", "r") as puzzle_input_file:
    for line in puzzle_input_file:
        line = line.strip()
        cycles_and_values = dict()
        
        if line.startswith("noop"):
            operation = "noop"
            
            cycles_and_values[cycle] = x_value
            cycle += 1
            cycles_and_values[cycle] = x_value
        else:
            operation, value = line.split()
            value = int(value)
            
            cycles_and_values[cycle] = x_value
            cycle += 1
            cycles_and_values[cycle] = x_value
            x_value += value
        
        print(cycles_and_values)
        cycle += 1
        for check_cycle in cycles_and_values:
            if check_cycle in important_cycles:
                result.append((check_cycle, cycles_and_values[check_cycle]))
print(cycle, x_value)
print(result)
#print(sum(result))
