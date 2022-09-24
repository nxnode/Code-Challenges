# https://www.codewars.com/kata/526571aae218b8ee490006f4


def freq_of_ones(number):
    numbers = []
    while number >= 1:
        numbers.append(number % 2)
        number = number // 2
    return numbers.count(1)
