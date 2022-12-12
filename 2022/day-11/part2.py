class Monkey:
    def __init__(self, index, starting_items, operation, test, throw_true, throw_false):
        self.index = index
        self.items = starting_items
        self.operation = operation # split into operation and number
        self.test = test # always divisible
        self.throw_true = throw_true
        self.throw_false = throw_false
    
    def add_item(self, new_item):
        self.items.append(item)
    
    def clear_items(self):
        self.items = list()
    
    def __str__(self):
        return f"Monkey has: \nIndex: {self.index}\nItems: {self.items}\nOperation: {self.operation}\nTest: {self.test}\nThrowTrue: {self.throw_true}\nThrowFalse: {self.throw_false}"


puzzle_input = list()
result = list()
monkeys = list()
monkey_inspect_counter = dict()
lcm = 1


with open("input.txt", "r") as puzzle_input_file:
    for line in puzzle_input_file:
        puzzle_input.append(line.strip())


line_index = 0
while line_index < len(puzzle_input):
    current_line = puzzle_input[line_index]
    if current_line.startswith("Monkey "):
        monkey_index = int(current_line.split()[-1][0])
        
        line_index += 1
        current_line = puzzle_input[line_index]
        starting_items = [int(item) for item in current_line.split("Starting items: ")[-1].split(", ")]
        
        line_index += 1
        current_line = puzzle_input[line_index]
        operation = current_line.split("Operation: new = old ")[-1].split()
        
        line_index += 1
        current_line = puzzle_input[line_index]
        test = int(current_line.split("Test: divisible by ")[-1])
        lcm *= test

        line_index += 1
        current_line = puzzle_input[line_index]
        throw_true = int(current_line.split("If true: throw to monkey ")[-1])

        line_index += 1
        current_line = puzzle_input[line_index]
        throw_false = int(current_line.split("If false: throw to monkey ")[-1])

        monkey = Monkey(monkey_index, starting_items, operation, test, throw_true, throw_false)
        monkeys.append(monkey)
    else:
        line_index += 1


important_rounds = [1, 20, 1000, 2000, 3000, 4000, 5000, 6000, 7000, 8000, 9000, 10000]
for i in range(10000):
    print(i)
    for monkey in monkeys:
        for item in monkey.items:
            #print(item)
            # count inspection
            monkey_inspect_counter[monkey.index] = monkey_inspect_counter.get(monkey.index, 0) + 1
            #print(f"inspecting item: {item}")

            operator, operand = monkey.operation
            if operand == "old":
                operand = item
            else:
                operand = int(operand)
            
            if operator == "+":
                item += operand
                #print(f"worry level increased to {item} by {operator} {operand}")
            elif operator == "*":
                item *= operand
                #print(f"worry level increased to {item} by {operator} {operand}")
            else:
                pass  # should never get here

            item %= lcm

            if item % monkey.test == 0:
                #print(f"worry level divisible by {test}, passing to {monkeys[monkey.throw_true].index}")
                monkeys[monkey.throw_true].add_item(item)
            else:
                #print(f"worry level not divisible by {test}, passing to {monkeys[monkey.throw_false].index}")
                monkeys[monkey.throw_false].add_item(item)
        
        monkey.clear_items()
        #print("\n")

    if i + 1 in important_rounds:
        print(monkey_inspect_counter)

monkey_counts = sorted([monkey_inspect_counter[monkey.index] for monkey in monkeys])
print(monkey_counts[-1] * monkey_counts[-2])