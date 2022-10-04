# https://www.codewars.com/kata/526571aae218b8ee490006f4

from code_challenges.code_wars.bit_counting import freq_of_ones


def test_freq_of_ones():
    assert freq_of_ones(0) == 0
    assert freq_of_ones(4) == 1
    assert freq_of_ones(7) == 3
    assert freq_of_ones(9) == 2
    assert freq_of_ones(10) == 2
