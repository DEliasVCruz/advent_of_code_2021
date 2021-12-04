from math import ceil


def total_digits_in_position(input_data, position):
    digits = []
    for line in input_data:
        digits.append(int(line[position]))
    total_digits = sum(digits)
    return total_digits


def filter_criteria_bit(total_digits, threshold, criteria):
    if criteria == "most":
        return str((total_digits >= threshold) * 1)
    return str((total_digits < threshold) * 1)


def filter_based_on_criteria(input_data, position, commonality):
    threshold = ceil(len(input_data) / 2)
    total_digits = total_digits_in_position(input_data, position)
    criteria = filter_criteria_bit(total_digits, threshold, commonality)
    filtered_data = []
    for line in input_data:
        if line[position] == criteria:
            filtered_data.append(line)
    return filtered_data


def convert_binary_to_decimal(binary):
    total = 0
    for digit in binary:
        total = total * 2 + int(digit)
    return total


if __name__ == "__main__":
    input_data = []
    with open("./input.txt", "r") as file:
        for line in file.read().splitlines():
            input_data.append(line)

    number_of_bits = len(input_data[0])
    oxygen_data = input_data
    co2_data = input_data

    for position in range(number_of_bits):
        if len(oxygen_data) != 1:
            oxygen_data = filter_based_on_criteria(oxygen_data, position, "most")
        if len(co2_data) != 1:
            co2_data = filter_based_on_criteria(co2_data, position, "least")

    oxygen_rate = convert_binary_to_decimal(oxygen_data[0])
    co2_rate = convert_binary_to_decimal(co2_data[0])

    print(oxygen_rate * co2_rate)
