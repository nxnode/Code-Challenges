# https://www.codewars.com/kata/54b42f9314d9229fd6000d9c/train/python

import pytest

from code_challenges.code_wars.duplicate_encoder import duplicate_encode


@pytest.mark.parametrize(
    "test_word,expected_word",
    [
        ("din", "((("),
        ("recede", "()()()"),
        ("Success", ")())())"),
        ("(( @", "))(("),
    ],
)
def test_duplicate_encode(test_word, expected_word):
    assert duplicate_encode(test_word) == expected_word
