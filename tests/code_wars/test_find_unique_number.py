# https://www.codewars.com/kata/585d7d5adb20cf33cb000235/train/python

from code_challenges.code_wars.find_unique_number import find_unique_number


def test_find_unique_number():
    test_numbers = {1: [1, 1, 1, 2, 1, 1], 2: [0, 0, 0.55, 0, 0]}
    assert find_unique_number(test_numbers[1]) == 2
    assert find_unique_number(test_numbers[2]) == 0.55
