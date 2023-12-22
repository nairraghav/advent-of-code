class Part:
    def __init__(self, x, m, a, s):
        self.x = x
        self.m = m
        self.a = a
        self.s = s

    @property
    def rating(self):
        return self.x + self.m + self.a + self.s


def get_input():
    workflows = list()
    parts = list()
    with open("input.txt", "r") as puzzle_input:
        list_to_use = workflows
        lines = puzzle_input.readlines()
        for line in lines:
            line = line.strip()
            if not line:
                list_to_use = parts
                continue
            list_to_use.append(line)
    
    return (workflows, parts)


def parse_workflows(workflows):
    result_workflows = dict()
    for workflow in workflows:
        start, flows = workflow.split("{")
        flows = flows[:-1]  # strip off last } character
        paths = list()
        for flow in flows.split(","):
            paths.append(flow)

        result_workflows[start] = tuple(paths)

    return result_workflows


def parse_parts(parts):
    result_parts = list()
    for part in parts:
        part_information = dict()
        for part_argument in part.strip("{}").split(","):
            key, value = part_argument.split("=")
            part_information[key] = int(value)
        result_parts.append(Part(**part_information))

    return result_parts


def get_final_path_for_part(part, workflows):
    current_workflow = "in"
    while current_workflow not in ("A", "R"):
        for workflow in workflows[current_workflow]:
            if ":" in workflow:
                flow_to_check, path = workflow.split(":")
                if "<" in flow_to_check:
                    part_parameter, value = flow_to_check.split("<")
                    value = int(value)
                    if getattr(part, part_parameter) < value:
                        current_workflow = path
                        break
                else:
                    part_parameter, value = flow_to_check.split(">")
                    value = int(value)
                    if getattr(part, part_parameter) > value:
                        current_workflow = path
                        break
            else:
                current_workflow = workflow
                break
    return current_workflow


def main():
    workflows, parts = get_input()
    workflows = parse_workflows(workflows)
    parts = parse_parts(parts)

    accepted_parts = list()
    for part in parts:
        if get_final_path_for_part(part, workflows) == "A":
            accepted_parts.append(part)
    
    print(sum([accepted_part.rating for accepted_part in accepted_parts]))


if __name__ == "__main__":
    main()