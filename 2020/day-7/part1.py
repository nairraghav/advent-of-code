"""
light red bags contain 1 bright white bag, 2 muted yellow bags.
"""

def bag_holds_golden_bag(bags, bag):
    bags_to_check = bags[bag]
    for bag_to_check in bags_to_check:
        if bag_to_check == "shiny gold bags":
            return True
        else:
            new_bags = bags.get(bag_to_check)
            if new_bags is not None:
                for new_bag in new_bags:
                    if new_bag not in bags_to_check:
                        bags_to_check.append(new_bag)
    
    return False    



bags = {}

with open("input.txt", "r") as puzzle_input:
    for line in puzzle_input:
        line.rstrip(".")
        containing_bag, contained_bags = line.split("contain")
        containing_bag = containing_bag.strip()
        contained_bags = contained_bags.strip()
        contained_bags = contained_bags.rstrip(".")
        contained_bags = contained_bags.split(",")
        cleaned_contained_bags = []
        for contained_bag in contained_bags:
            contained_bag = contained_bag.strip()
            if contained_bag[-1] != "s":
                contained_bag = contained_bag + "s"
            
            try:
                int(contained_bag[0])
                contained_bag = contained_bag[2:]
            except:
                pass
            cleaned_contained_bags.append(contained_bag)
            bags[containing_bag] = cleaned_contained_bags

    print(bags)
    number_of_bags_holding_golden_bag = 0
    for bag in bags:
        if bag_holds_golden_bag(bags, bag):
            number_of_bags_holding_golden_bag += 1

    print(number_of_bags_holding_golden_bag)