"""
class: 1-3 or 5-7
row: 6-11 or 33-44
seat: 13-40 or 45-50

your ticket:
7,1,14

nearby tickets:
7,3,47
40,4,50
55,2,20
38,6,12
"""

section = 1
rules = []
my_ticket = []
nearby_tickets = []
with open("input.txt", "r") as puzzle_input:
    for line in puzzle_input:
        line = line.strip()
        if section == 1:
            if line != "":
                rules.append(line.split(": ")[1])
        elif section == 2:
            if "ticket" not in line and line != "":
                my_ticket.append(line)
        elif section == 3:
            if "ticket" not in line:
                nearby_tickets.append(line)

        if line == "":
            section += 1

min_max_rules = []
for rule in rules:
    rule_start, rule_end = rule.split(" or ")
    for start_end in (rule_start, rule_end):
        start, end = start_end.split("-")
        min_max_rules.append((int(start), int(end)))


bad_tickets = []


for tickets in nearby_tickets:
    tickets = tickets.split(",")
    for ticket in tickets:
        ticket = int(ticket)
        bad_ticket = True
        for min_rule, max_rule in min_max_rules:
            if (ticket >= min_rule) and (ticket <= max_rule):
                bad_ticket = False
                break
        if bad_ticket:
            bad_tickets.append(ticket)

#print(min_max_rules)
print(bad_tickets)
print(sum(bad_tickets))