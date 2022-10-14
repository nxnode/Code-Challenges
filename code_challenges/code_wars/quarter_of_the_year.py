# https://www.codewars.com/kata/5ce9c1000bab0b001134f5af


def find_quarter(month):
    if month < 4:
        return 1
    elif month < 7:
        return 2
    elif month <= 9:
        return 3
    else:
        return 4
