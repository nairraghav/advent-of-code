puzzle_input_list = []

with open("input.txt", "r") as puzzle_input:
    for line in puzzle_input:
        for digit in line:
            puzzle_input_list.append(int(digit))

width = 25
height = 6
digits_per_layer = width*height

layers = [[puzzle_input_list[0]]]

counter = 1
for digit in puzzle_input_list[1:]:
    if counter % digits_per_layer == 0:
        layers.append([digit])
    else:
        layers[-1].append(digit)

    counter += 1

final_result = []
for index in range(width*height):
    for layer in layers:
        if layer[index] in (0,1):
            final_result.append(layer[index])
            break
assert len(final_result) == width*height

final_final_result = [[]]
counter = 0
for digit in final_result:
    if counter == width:
        final_final_result.append([digit])
        counter = 1
    else:
        final_final_result[-1].append(digit)
        counter += 1

print(final_final_result)


for h in range(0,height):
    for w in range(0,width):
        if final_final_result[h][w] == 1:
            print('*',end='')
        else:
            print(' ',end='')
    print()

"""
 **    ** *   *****  **  
*  *    * *   **    *  * 
*       *  * * ***  *  * 
* **    *   *  *    **** 
*  * *  *   *  *    *  * 
 ***  **    *  **** *  * 
"""    