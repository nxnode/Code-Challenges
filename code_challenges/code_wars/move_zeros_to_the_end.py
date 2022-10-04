# https://www.codewars.com/kata/52597aa56021e91c93000cb0


def move_zeros_to_end(numbers):
    for number in numbers:
        if number == 0:
            numbers.remove(number)
            numbers.append(number)
    return numbers
