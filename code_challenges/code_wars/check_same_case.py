# https://www.codewars.com/kata/5dd462a573ee6d0014ce715b
def evaluate_characters_case(a, b):
    if not a.isalpha() or not b.isalpha():
        return -1
    elif a.isupper() == b.isupper():
        return 1
    else:
        return 0
