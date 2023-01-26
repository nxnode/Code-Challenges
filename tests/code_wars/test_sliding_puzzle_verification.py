# https://www.codewars.com/kata/5e28b3ff0acfbb001f348ccc/train/python
import pytest

from code_challenges.code_wars.sliding_puzzle_verification import is_solved


@pytest.mark.parametrize(
    "test_matrix, expected_boolean",
    [
        (([[0, 1], [2, 3]]), True),
        (([[1, 0], [3, 2]]), False),
    ],
)
def test_is_solved(test_matrix, expected_boolean):
    assert is_solved(test_matrix) == expected_boolean
