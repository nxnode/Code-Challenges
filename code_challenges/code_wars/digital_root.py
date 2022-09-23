# https://www.codewars.com/kata/541c8630095125aba6000c00


def digital_root(number):
    while number > 9:
        sum_of_digit = 0
        for digit in str(number):
            sum_of_digit += int(digit)
        number = sum_of_digit
    return number
