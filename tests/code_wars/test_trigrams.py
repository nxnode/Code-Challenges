# https://www.codewars.com/kata/55d8dc4c8e629e55dc000068

from code_challenges.code_wars.trigrams import extract_trigrams


def test_extract_trigram():
    assert (
        extract_trigrams("the quick red")
        == "the he_ e_q _qu qui uic ick ck_ k_r _re red"
    )
    assert extract_trigrams("Hi") == ""
