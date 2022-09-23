# https://www.codewars.com/kata/525f50e3b73515a6db000b83


def phone_format(numbers):
    numbers = "".join(str(i) for i in numbers)
    return f"({numbers[0:3]}) {numbers[3:6]}-{numbers[6:]}"
