# https://www.codewars.com/kata/55bf01e5a717a0d57e0000ec

from code_challenges.code_wars.persistent_bugger import persistence


def test_persistence():
    assert persistence(39) == 3
    assert persistence(4) == 0
    assert persistence(25) == 2
    assert persistence(999) == 4
