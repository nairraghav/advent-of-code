import re
running_sum = 0

with open("input.txt", "r") as puzzle_input:
    lines = puzzle_input.readlines()

    for line in lines:
        do_matches = [match.end(0) for match in re.finditer("do\(\)", line)]
        dont_matches = [match.start(0) for match in re.finditer("don\'t\(\)", line)]
        print("do_matches")
        print(do_matches)
        print("dont_matches")
        print(dont_matches)
        
        print("bad_ranges")
        bad_ranges = list()
        for dont_match in dont_matches:
            no_matches = True
            for do_match in do_matches:
                if do_match > dont_match:
                    bad_ranges.append((dont_match, do_match))
                    no_matches = False
                    break
            if no_matches:
                bad_ranges.append((dont_match, len(line)))
                break
        print(bad_ranges)


        matches = re.finditer("mul\([0-9]{1,3},[0-9]{1,3}\)", line)
        for match in matches:
            bad_range = False
            for bad_range_start, bad_range_end in bad_ranges:
                print(bad_range_start, bad_range_end, match.start(0))
                if bad_range_start < match.start(0) < bad_range_end:
                    bad_range = True
                    break
            if not bad_range:
                matched_string = line[match.start(0): match.end(0)]
                matched_string = matched_string[4:-1]
                matched_string = matched_string.split(",")
                running_sum += int(matched_string[0]) * int(matched_string[1])
    
print(running_sum)