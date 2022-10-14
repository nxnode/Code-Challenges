# https://www.codewars.com/kata/5ce9c1000bab0b001134f5af

from code_challenges.code_wars.quarter_of_the_year import find_quarter


def test_find_quarter():
    assert find_quarter(3) == 1
    assert find_quarter(5) == 2
    assert find_quarter(8) == 3
    assert find_quarter(11) == 4
