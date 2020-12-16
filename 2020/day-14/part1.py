def get_sum_of_memory(mask, memory_to_values):
    for memory,value in memory_to_values.items():
        expanded_value = f"{value:036b}"
        new_value = ""
        for index in range(36):
            if mask[index] == "X":
                new_value += expanded_value[index]
            else:
                new_value += mask[index]
        memory_to_values[memory] = int(new_value, 2)

    return memory_to_values


with open("input.txt", "r") as puzzle_input:
    masks_and_memory_to_values = []
    memory_to_values = {}
    mask = ""
    mask_set = False
    for line in puzzle_input:
        line = line.strip()
        
        if line.startswith("mask"):
            if mask != "":
                masks_and_memory_to_values.append((mask, memory_to_values))
            memory_to_values = {}
            mask = line.split("= ")[1]
        else:
            memory = line.split("[")[1]
            memory = memory.split("]")[0]
            value = int(line.split("= ")[1])
            memory_to_values[memory] = value

    masks_and_memory_to_values.append((mask, memory_to_values))
    
final_memory_to_values = {}
for item in masks_and_memory_to_values:
    new_memory_to_values = get_sum_of_memory(item[0], item[1])
    final_memory_to_values = {**final_memory_to_values, **new_memory_to_values}

total = 0
for _, value in final_memory_to_values.items():
    total += value
print(total)
