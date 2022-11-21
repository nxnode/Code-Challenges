# https://www.codewars.com/kata/54bf1c2cd5b56cc47f0007a1

from code_challenges.code_wars.count_duplicates import count_duplicates


def test_count_duplicates():
    assert count_duplicates("") == 0
    # assert count_duplicates("abcde") == 0
    # assert count_duplicates("abcdeaa") == 1
    # assert count_duplicates("abcdeaB") == 2
    # assert count_duplicates("Indivisibilities") == 2
