# https://www.codewars.com/kata/585d7d5adb20cf33cb000235/train/python


def find_unique_number(numbers):
    # new_numbers = numbers
    # for n in numbers:
    #     number_count = 0
    #     for y in new_numbers:
    #         if n == y:
    #             number_count += 1
    #     if number_count == 1:
    #         return n
    ## commented out version passed 11 of 12 - failed the big number test

    frequency_of_numbers = {}
    for single_number in numbers:
        if single_number in frequency_of_numbers:
            frequency_of_numbers[single_number] += 1
        else:
            frequency_of_numbers[single_number] = 1
    frequency_of_one = [k for (k, v) in frequency_of_numbers.items() if v == 1]
    return frequency_of_one[0]
