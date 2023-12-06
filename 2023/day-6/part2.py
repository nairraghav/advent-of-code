def main():
    time = 0
    distance = 0
    with open("input.txt", "r") as puzzle_input:
        lines = puzzle_input.readlines()
        time = int("".join(lines[0].split()[1:]))
        distance = int("".join(lines[1].split()[1:]))
    
    print(time)
    print(distance)

    possible_finish_counter = 0
    for time_to_press in range(time+1):
        distance_covered = time_to_press * (time - time_to_press)
        if distance_covered > distance:
            print(time, time_to_press, distance)
            possible_finish_counter += 1
    
    print(possible_finish_counter)


if __name__ == "__main__":
    main()