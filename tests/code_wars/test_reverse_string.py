# https://www.codewars.com/kata/5264d2b162488dc400000001

from code_challenges.code_wars.reverse_string import reverse_larger_strings


def test_reverse_larger_strings():
    assert reverse_larger_strings("Welcome") == "emocleW"
    assert reverse_larger_strings("to") == "to"
    assert reverse_larger_strings("CodeWars") == "sraWedoC"
    assert reverse_larger_strings("Hey fellow warriors") == "Hey wollef sroirraw"
    assert (
        reverse_larger_strings("This sentence is a sentence")
        == "This ecnetnes is a ecnetnes"
    )
