# https://www.codewars.com/kata/57eb8fcdf670e99d9b000272/train/python
import pytest

from code_challenges.code_wars.highest_scoring_word import highest_word


@pytest.mark.parametrize(
    "test_words,expected_word",
    [
        ("man i need a taxi up to ubud", "taxi"),
        ("what time are we climbing up the volcano", "volcano"),
        ("take me to semynak", "semynak"),
        ("aa b", "aa"),
        ("b aa", "b"),
        ("bb d", "bb"),
        ("d bb", "d"),
        ("aaa b", "aaa"),
    ],
)
def test_highest_word(test_words, expected_word):
    assert highest_word(test_words) == expected_word
