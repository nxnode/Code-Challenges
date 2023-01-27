# https://www.codewars.com/kata/550f22f4d758534c1100025a/python

import pytest

from code_challenges.code_wars.directions_reduction import directions_reduction


@pytest.mark.parametrize(
    "test_directions,expected_directions",
    [
        (["NORTH", "SOUTH", "SOUTH", "EAST", "WEST", "NORTH", "WEST"], ["WEST"]),
        (["NORTH", "WEST", "SOUTH", "EAST"], ["NORTH", "WEST", "SOUTH", "EAST"]),
    ],
)
def test_directions_reduced(test_directions, expected_directions):
    assert directions_reduction(test_directions) == expected_directions
