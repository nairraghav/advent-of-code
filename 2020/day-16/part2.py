section = 1
rules = []
my_ticket = []
nearby_tickets = []
with open("input.txt", "r") as puzzle_input:
    for line in puzzle_input:
        line = line.strip()
        if section == 1:
            if line != "":
                rules.append(line.split(": "))
        elif section == 2:
            if "ticket" not in line and line != "":
                my_ticket.append(line)
        elif section == 3:
            if "ticket" not in line:
                nearby_tickets.append(line)

        if line == "":
            section += 1

name_to_rules = {}
for name, rule in rules:
    rule_start, rule_end = rule.split(" or ")
    min_max_rules = []
    for start_end in (rule_start, rule_end):
        start, end = start_end.split("-")
        min_max_rules.append((int(start), int(end)))
    name_to_rules[name] = min_max_rules

good_tickets = []

print(name_to_rules)

for tickets in nearby_tickets:
    tickets = [int(ticket) for ticket in tickets.split(",")]
    for ticket in tickets:
        ticket = int(ticket)
        all_rules_failed = True    
        for _, min_max_rules in name_to_rules.items():
            for min_rule, max_rule in min_max_rules:
                if (ticket >= min_rule) and (ticket <= max_rule):
                    all_rules_failed = False
                    break
            if not all_rules_failed:
                break
        if not all_rules_failed:
                break
    if all_rules_failed:
        good_tickets.append(tickets)


print(good_tickets)


