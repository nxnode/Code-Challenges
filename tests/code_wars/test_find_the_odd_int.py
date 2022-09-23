# https://www.codewars.com/kata/54da5a58ea159efa38000836

from code_challenges.code_wars.find_the_odd_int import least_freq_num


def test_least_freq_num():
    assert least_freq_num([20, 1, -1, 2, -2, 3, 3, 5, 5, 1, 2, 4, 20, 4, -1, -2, 5]) == 5
    assert least_freq_num([1, 1, 2, -2, 5, 2, 4, 4, -1, -2, 5]) == -1
    assert least_freq_num([20, 1, 1, 2, 2, 3, 3, 5, 5, 4, 20, 4, 5]) == 5
    assert least_freq_num([10]) == 10
    assert least_freq_num([10, 10, 10]) == 10
    assert least_freq_num([1, 1, 1, 1, 1, 1, 10, 1, 1, 1, 1]) == 10
    assert least_freq_num([5, 4, 3, 2, 1, 5, 4, 3, 2, 10, 10]) == 1
