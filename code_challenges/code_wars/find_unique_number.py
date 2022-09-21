# https://www.codewars.com/kata/585d7d5adb20cf33cb000235/train/python


def find_unique_number(numbers):
    freq_of_numbers = {}
    for number in numbers:
        freq_of_numbers[number] = freq_of_numbers.get(number, 0) + 1
    freq_of_one = [num for num, count in freq_of_numbers.items() if count == 1]
    return freq_of_one[0]
