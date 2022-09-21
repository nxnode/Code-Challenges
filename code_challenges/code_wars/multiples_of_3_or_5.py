# https://www.codewars.com/kata/514b92a657cdc65150000006/train/python


def factor_of_3_or_5(number):
    number -= 1
    multiple_of_either = set()
    while number > 0:
        if number % 3 == 0 or number % 5 == 0:
            multiple_of_either.add(number)
        number -= 1
    return sum(multiple_of_either)
