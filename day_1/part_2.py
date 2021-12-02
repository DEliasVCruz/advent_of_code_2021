if __name__ == "__main__":
    with open("./day1_part1_input.txt", "r") as f:
        data = [int(line[:-1]) for line in f]

    increments = 0
    position = 0
    previous_messurement_sum = 0
    while position < len(data) - 2:
        current_messurement_sum = sum(data[position:position + 3])
        if current_messurement_sum > previous_messurement_sum:
            increments += 1
        previous_messurement_sum = current_messurement_sum
        position += 1

    print(increments - 1)
