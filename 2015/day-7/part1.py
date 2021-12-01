"""
x << y
    Returns x with the bits shifted to the left by y places (and new bits on the right-hand-side are zeros). This is the same as multiplying x by 2**y. 
x >> y
    Returns x with the bits shifted to the right by y places. This is the same as //'ing x by 2**y. 
x & y
    Does a "bitwise and". Each bit of the output is 1 if the corresponding bit of x AND of y is 1, otherwise it's 0. 
x | y
    Does a "bitwise or". Each bit of the output is 0 if the corresponding bit of x AND of y is 0, otherwise it's 1. 
~ x
    Returns the complement of x - the number you get by switching each 1 for a 0 and each 0 for a 1. This is the same as -x - 1. 
x ^ y
    Does a "bitwise exclusive or". Each bit of the output is the same as the corresponding bit in x if that bit in y is 0, and it's the complement of the bit in x if that bit in y is 1. 


"""

wires = dict()
operations = {"AND", "OR", "LSHIFT", "RSHIFT"}
with open("input.txt", "r") as puzzle_input:
    for line in puzzle_input:
        line = line.strip()
        expression, wire = line.split(" -> ")
        do_operation = False
        for operation in operations:
            if operation in line:
                do_operation = True
                break
        if do_operation is True:
            first_wire, operation, second_wire = expression.split()
            print(wires)
            print(first_wire, operation, second_wire)
            if operation == "AND":
                result = wires.get(first_wire) & wires.get(second_wire)
            elif operation == "OR":
                result = wires.get(first_wire) | wires.get(second_wire)
            elif operation == "LSHIFT":
                result = wires.get(first_wire) << int(second_wire)
            elif operation == "RSHIFT":
                result = wires.get(first_wire) >> int(second_wire)
            else:
                raise Exception(f"Operation Not Supported: {operation}")
        else:
            if expression.startswith("NOT"):
                wire_value = wires.get(expression.split()[-1])
                result = ~ wire_value
            else:
                # last case is just assignment
                result = int(expression)
        wires[wire] = result

print(wires)
print(wires[a])
            