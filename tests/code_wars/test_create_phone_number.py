# https://www.codewars.com/kata/525f50e3b73515a6db000b83

from code_challenges.code_wars.create_phone_number import phone_format


def test_phone_format():
    assert phone_format([1, 2, 3, 4, 5, 6, 7, 8, 9, 0]) == "(123) 456-7890"
    assert phone_format([1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == "(111) 111-1111"
    assert phone_format([1, 2, 3, 4, 5, 6, 7, 8, 9, 0]) == "(123) 456-7890"
    assert phone_format([0, 2, 3, 0, 5, 6, 0, 8, 9, 0]) == "(023) 056-0890"
    assert phone_format([0, 0, 0, 0, 0, 0, 0, 0, 0, 0]) == "(000) 000-0000"
