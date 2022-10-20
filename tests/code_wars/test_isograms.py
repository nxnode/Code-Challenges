# https://www.codewars.com/kata/54ba84be607a92aa900000f1

from code_challenges.code_wars.isograms import isograms


def test_isograms():
    assert isograms("Dermatoglyphics") is True
    assert isograms("isogram") is True
    assert isograms("aba") is False
    assert isograms("moOse") is False
    assert isograms("isIsogram") is False
    assert isograms("") is True
