if __name__ == "__main__":
    input_data = []
    with open("./input.txt", "r") as file:
        for line in file.read().splitlines():
            input_data.append(line)

    digits = {}
    for line in input_data:
        for position, digit in enumerate(line):
            if position not in digits:
                digits[position] = []
            digits[position].append(int(digit))

    gama_total = 0
    epsilon_total = 0
    for position in digits:
        if sum(digits[position]) < (len(input_data) / 2):
            gama_digit = 0
            epsilon_digit = 1
        else:
            gama_digit = 1
            epsilon_digit = 0
        gama_total = gama_total * 2 + gama_digit
        epsilon_total = epsilon_total * 2 + epsilon_digit

    power_consumption = gama_total * epsilon_total
    print(power_consumption)
