# https://www.codewars.com/kata/54ff3102c1bad923760001f3

from code_challenges.code_wars.vowel_count import vowel_count


def test_vowel_count():
    assert vowel_count("aeiou") == 5
    assert vowel_count("y") == 0
    assert vowel_count("bcdfghjklmnpqrstvwxz y") == 0
    assert vowel_count("") == 0
    assert vowel_count("abracadabra") == 5
