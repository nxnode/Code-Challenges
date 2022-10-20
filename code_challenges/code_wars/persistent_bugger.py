# https://www.codewars.com/kata/55bf01e5a717a0d57e0000ec


def persistence(number):
    persistence_count = 0
    while len(str(number)) > 1:
        persistence_count += 1
        product = 1
        for num in str(number):
            product *= int(num)
        number = product
    return persistence_count
