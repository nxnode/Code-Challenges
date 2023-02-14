# https://www.codewars.com/kata/5839c48f0cf94640a20001d3/train/python
import pytest

from code_challenges.code_wars.land_perimeter import perimeter


@pytest.mark.parametrize(
    "test_maps, expected_count",
    [
        (
            [
                "OXOOOX",
                "OXOXOO",
                "XXOOOX",
                "OXXXOO",
                "OOXOOX",
                "OXOOOO",
                "OOXOOX",
                "OOXOOO",
                "OXOOOO",
                "OXOOXX",
            ],
            "Total land perimeter: 60",
        ),
        (
            [
                "OXOOO",
                "OOXXX",
                "OXXOO",
                "XOOOO",
                "XOOOO",
                "XXXOO",
                "XOXOO",
                "OOOXO",
                "OXOOX",
                "XOOOO",
                "OOOXO",
            ],
            "Total land perimeter: 52",
        ),
        (
            ["XXXXXOOO", "OOXOOOOO", "OOOOOOXO", "XXXOOOXO", "OXOXXOOX"],
            "Total land perimeter: 40",
        ),
        (
            [
                "XOOOXOO",
                "OXOOOOO",
                "XOXOXOO",
                "OXOXXOO",
                "OOOOOXX",
                "OOOXOXX",
                "XXXXOXO",
            ],
            "Total land perimeter: 54",
        ),
        (
            ["OOOOXO", "XOXOOX", "XXOXOX", "XOXOOO", "OOOOOO", "OOOXOO", "OOXXOO"],
            "Total land perimeter: 40",
        ),
    ],
)
def test_perimeter(test_maps, expected_count):
    assert perimeter(test_maps) == expected_count
