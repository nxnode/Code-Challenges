# https://www.codewars.com/kata/52b7ed099cdc285c300001cd

from code_challenges.code_wars.sum_of_intervals import sum_of_intervals


def test_sum_of_intervals():
    assert sum_of_intervals([(1, 5)]) == 4
    assert sum_of_intervals([(1, 5), (6, 10)]) == 8
    assert sum_of_intervals([(1, 5), (1, 5)]) == 4
    assert sum_of_intervals([(1, 4), (7, 10), (3, 5)]) == 7
