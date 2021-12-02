if __name__ == "__main__":

    horizontal_position = 0
    depth = 0
    with open("./input.txt", "r") as file:
        for line in file.read().splitlines():
            movement = line.split(' ')[0]
            degree = int(line.split(' ')[1])
            if movement == 'forward':
                horizontal_position += degree
            elif movement == 'down':
                depth += degree
            else:
                depth -= degree

    print(depth * horizontal_position)
