if __name__ == "__main__":
    current_line = 0
    previous_line = 0
    increments = 0
    with open("./input.txt", "r") as f:
        for line in f.read().splitlines():
            current_line = int(line)
            if current_line > previous_line:
                increments += 1
            previous_line = current_line

    print(increments - 1)
