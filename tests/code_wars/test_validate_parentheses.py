# https://www.codewars.com/kata/52774a314c2333f0a7000688

from code_challenges.code_wars.validate_parentheses import validate_parentheses


def test_validate_parentheses():
    assert validate_parentheses("  (") == False
    assert validate_parentheses(")test") == False
    assert validate_parentheses("") == True
    assert validate_parentheses("hi())(") == False
    assert validate_parentheses("hi(hi)()") == True
    assert validate_parentheses(")))(((") == False
