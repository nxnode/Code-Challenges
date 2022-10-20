# https://www.codewars.com/kata/554b4ac871d6813a03000035

from code_challenges.code_wars.highest_and_lowest import max_and_min


def test_max_and_min():
    assert max_and_min("8 3 -5 42 -1 0 0 -9 4 7 4 -4") == "42 -9"
    assert max_and_min("1 2 3") == "3 1"
    assert (
        max_and_min("10 9 8 7 6 5 4 3 2 1 -10 -9 -8 -7 -6 -5 -4 -3 -2 -1 ") == "10 -10"
    )
