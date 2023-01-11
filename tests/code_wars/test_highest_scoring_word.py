# https://www.codewars.com/kata/57eb8fcdf670e99d9b000272/train/python

from code_challenges.code_wars.highest_scoring_word import highest_word

def test_highest_word():
    assert highest_word('man i need a taxi up to ubud') == 'taxi'
    assert highest_word('what time are we climbing up the volcano') == 'volcano'
    assert highest_word('take me to semynak') == 'semynak'
    assert highest_word('aa b') == 'aa'
    assert highest_word('b aa') == 'b'
    assert highest_word('bb d') == 'bb'
    assert highest_word('d bb') == 'd'
    assert highest_word("aaa b") == "aaa"