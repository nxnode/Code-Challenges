# https://www.codewars.com/kata/54da5a58ea159efa38000836


def odd_freq(numbers):
    freq_of_numbers = {}
    for number in numbers:
        freq_of_numbers[number] = freq_of_numbers.get(number, 0) + 1
    freq_of_one = [
        num for num, count in freq_of_numbers.items() if not (count % 2) == 0
    ]
    return freq_of_one[0]
