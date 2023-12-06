def main():
    times = list()
    distances = list()
    with open("input.txt", "r") as puzzle_input:
        lines = puzzle_input.readlines()
        times = [int(field) for field in lines[0].split()[1:]]
        distances = [int(field) for field in lines[1].split()[1:]]
    
    print(times)
    print(distances)

    running_product = 1
    
    for index in range(len(times)):
        possible_finish_counter = 0
        time = times[index]
        distance = distances[index]

        for time_to_press in range(time+1):
            distance_covered = time_to_press * (time - time_to_press)
            if distance_covered > distance:
                print(time, time_to_press, distance)
                possible_finish_counter += 1
        
        print(possible_finish_counter)    
        running_product *= possible_finish_counter
    
    print(running_product)


if __name__ == "__main__":
    main()