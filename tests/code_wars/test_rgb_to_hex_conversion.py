# https://www.codewars.com/kata/513e08acc600c94f01000001/train/python

import pytest

from code_challenges.code_wars.rgb_to_hex_conversion import rgb_to_hex


@pytest.mark.parametrize(
    "test_rgb,expected_hex",
    [
        ("0, 0, 0", "000000"),
        ("1, 2, 3", "010203"),
        ("255, 255, 255", "FFFFFF"),
        ("254, 253, 252", "FEFDFC"),
        ("-20, 275, 125", "00FF7D"),
    ],
)
def test_rgb_to_hex(test_rgb, expected_hex):
    assert rgb_to_hex(test_rgb) == expected_hex
