# https://www.codewars.com/kata/585d7d5adb20cf33cb000235/train/python


def find_unique_number(numbers):
    frequency_of_numbers = {}
    for single_number in numbers:
        frequency_of_numbers[single_number] = (
            frequency_of_numbers.get(single_number, 0) + 1
        )
        # if single_number in frequency_of_numbers:
        #     frequency_of_numbers[single_number] += 1
        # else:
        #     frequency_of_numbers[single_number] = 1
    frequency_of_one = [
        num for num, count in frequency_of_numbers.items() if count == 1
    ]
    return frequency_of_one[0]
