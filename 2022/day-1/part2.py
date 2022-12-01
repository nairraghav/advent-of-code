import heapq

puzzle_input_list = []
current_count = 0

with open("input.txt", "r") as puzzle_input:

    for line in puzzle_input:
        try:
            current_count += int(line)
        except ValueError:
            puzzle_input_list.append(current_count)
            current_count = 0

    puzzle_input_list.append(current_count)


# to make a max heap, we use negative values
puzzle_input_list = [-1 * item for item in puzzle_input_list]

heapq.heapify(puzzle_input_list)

running_sum = 0
for _ in range(3):  # only needed top 3
    current_item = heapq.heappop(puzzle_input_list)
    running_sum += current_item

# need to cancel out the negative from using the heap
running_sum = -1 * running_sum

print(running_sum)
