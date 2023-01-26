# https://www.codewars.com/kata/525f3eda17c7cd9f9e000b39/train/python

from code_challenges.code_wars.calculating_with_functions import (
    zero,
    one,
    two,
    three,
    four,
    five,
    six,
    seven,
    eight,
    nine,
    plus,
    minus,
    times,
    divided_by,
)


def test_calc_functions():
    assert one(plus(two())) == 3
    assert seven(times(five())) == 35
    assert four(plus(nine())) == 13
    assert eight(minus(three())) == 5
    assert six(divided_by(two())) == 3
    assert zero(plus(three())) == 3
    assert one(divided_by(nine())) == 9
