# https://www.codewars.com/kata/5a19226646d843de9000007d/train/python

from code_challenges.code_wars.how_may_unique_consonants import count_consonants

def test_count_consonants():
    assert count_consonants('sillystring') == 7
    assert count_consonants('aeiou') == 0
    assert count_consonants('abcdefghijklmnopqrstuvwxyz') == 21
    assert count_consonants('Count my unique consonants!!') == 7
    