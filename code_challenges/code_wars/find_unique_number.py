# https://www.codewars.com/kata/585d7d5adb20cf33cb000235/train/python


def find_unique_number(numbers):
    new_numbers = numbers
    for n in numbers:
        number_count = 0
        for y in new_numbers:
            if n == y:
                number_count += 1
        if number_count == 1:
            return n


## passed 11 of 12 - failed the big number test
