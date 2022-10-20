# https://www.codewars.com/kata/5526fc09a1bbd946250002dc


def parity_outlier(numbers):
    even_int = 0
    odd_int = 0

    for num in numbers:
        if num % 2 == 0:
            even_int += 1
            if even_int > 1:
                for num in numbers:
                    if num % 2 != 0:
                        return num
        else:
            odd_int += 1
            if odd_int > 1:
                for num in numbers:
                    if num % 2 == 0:
                        return num
