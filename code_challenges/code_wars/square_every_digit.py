# https://www.codewars.com/kata/546e2562b03326a88e000020


def square_every_digit(digits):
    squared_nums = ""
    for num in str(digits):
        squared_nums += f"{int(num) * int(num)}"
    return int(squared_nums)
