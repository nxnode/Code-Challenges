# https://www.codewars.com/kata/546e2562b03326a88e000020

from code_challenges.code_wars.square_every_digit import square_every_digit


def test_square_every_digit():
    assert square_every_digit(9119) == 811181
    assert square_every_digit(0) == 0
