# https://www.codewars.com/kata/5526fc09a1bbd946250002dc

from code_challenges.code_wars.find_the_parity_outlier import parity_outlier


def test_parity_outlier():
    assert parity_outlier([2, 4, 6, 8, 10, 3]) == 3
    assert parity_outlier([2, 4, 0, 100, 4, 11, 2602, 36]) == 11
    assert parity_outlier([160, 3, 1719, 19, 11, 13, -21]) == 160
