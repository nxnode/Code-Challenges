# https://www.codewars.com/kata/5dd462a573ee6d0014ce715b
# Write a function that will check if two given characters are the same case.
#
# If either of the characters is not a letter, return -1
# If both characters are the same case, return 1
# If both characters are letters, but not the same case, return 0
#
# Examples
# 'a' and 'g' returns 1
# 'A' and 'C' returns 1
# 'b' and 'G' returns 0
# 'B' and 'g' returns 0
# '0' and '?' returns -1

from code_challenges.code_wars.check_same_case import evaluate_characters_case

def test_case():
    data = (
        ('C', 'B', 1),
        ('b', 'A', 0),
        ('d', 'd', 1),
        ('A', 's', 0),
        ('c', 'B', 0),
        ('b', 'Z', 0),
        ('\t', 'Z', -1),
        ('H', ':', -1))

    for (a, b, eq) in data:
        assert evaluate_characters_case(a, b) == eq
