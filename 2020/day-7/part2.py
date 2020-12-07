"""
light red bags contain 1 bright white bag, 2 muted yellow bags.
"""

def bags_within_bag(bags, bag):
    number_of_bags = 0
    for bag_to_check in bags[bag]:
        if bag_to_check == "no other bags":
            return 1, False
        else:
            num_of_checked_bag = int(bag_to_check[0])
            number_of_bags_inside, not_last_bag = bags_within_bag(bags, bag_to_check[2:])
            number_of_bags += num_of_checked_bag * number_of_bags_inside
            if not_last_bag:
                number_of_bags += num_of_checked_bag
    return number_of_bags, True


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
            
            cleaned_contained_bags.append(contained_bag)
            bags[containing_bag] = cleaned_contained_bags

    print(bags_within_bag(bags, "shiny gold bags")[0])