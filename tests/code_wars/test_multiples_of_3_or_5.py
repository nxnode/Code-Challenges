# https://www.codewars.com/kata/514b92a657cdc65150000006/train/python

from code_challenges.code_wars.multiples_of_3_or_5 import factor_of_3_or_5


def test_factor_of_3_or_5():
    assert factor_of_3_or_5(4) == 3
    assert factor_of_3_or_5(6) == 8
    assert factor_of_3_or_5(16) == 60
    assert factor_of_3_or_5(3) == 0
    assert factor_of_3_or_5(5) == 3
    assert factor_of_3_or_5(15) == 45
    assert factor_of_3_or_5(0) == 0
    assert factor_of_3_or_5(1) == 0
    assert factor_of_3_or_5(10) == 23
    assert factor_of_3_or_5(20) == 78
    assert factor_of_3_or_5(200) == 9168
