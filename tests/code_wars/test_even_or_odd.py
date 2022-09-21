# https://www.codewars.com/kata/53da3dbb4a5168369a0000fe

from code_challenges.code_wars.even_or_odd import even_or_odd


def test_even_or_odd():
    assert even_or_odd(1) == "Odd"
    assert even_or_odd(2) == "Even"
    assert even_or_odd(333) == "Odd"
    assert even_or_odd(444) == "Even"
    assert even_or_odd(5678967) == "Odd"
    assert even_or_odd(-748657) == "Odd"
    assert even_or_odd(2452343) == "Odd"
    assert even_or_odd(1000892) == "Even"
    assert even_or_odd(19561767824613) == "Odd"
    assert even_or_odd(995456734653456244) == "Even"
    assert even_or_odd(6782634872143876) == "Even"
