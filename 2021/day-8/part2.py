# incomplete solution
puzzle_input_list = []

with open("input.txt", "r") as puzzle_input:
    for line in puzzle_input:
        line = line.strip()
        input_string, output_string = line.split(" | ")
        inputs = input_string.split()
        outputs = output_string.split()
        puzzle_input_list.append([inputs, outputs])


acedgfb cdfbe gcdfa fbcad dab cefabd cdfgeb eafb cagedb ab |
cdfeb fcadb cdfeb cdbaf


normal:
0 - abcefg
1 - cf (unique)
2 - acdeg
3 - acdfg
4 - bcdf (unique)
5 - abdfg
6 - abdefg
7 - acf (unique)
8 - abcdefg (unique)
9 - abcdfg

mapped:
0 -
1 - ab (we know ab -> cf)
2 - 
3 - 
4 - eafb (we know ef -> bd)
5 - 
6 -
7 - dab (with this, we know a -> d)
8 - acedgfb
9 -

unknown:
cdfbe gcdfa fbcad cefabd cdfgeb cagedb
sorted to:
bcdef acdfg abcdf abcdef bcdefg abcdeg
2,3,5 -> bcdef, acdfg, abcdf
0,6,9 -> abcdef, bcdefg, abcdeg