if __name__ == "__main__":

    horizontal_position = 0
    depth = 0
    aim = 0
    with open("./input.txt", "r") as file:
        for line in file.read().splitlines():
            movement = line.split(" ")[0]
            degree = int(line.split(" ")[1])
            if movement == "down":
                aim += degree
            elif movement == "up":
                aim -= degree
            else:
                horizontal_position += degree
                depth += aim * degree

    print(depth * horizontal_position)
