# https://www.codewars.com/kata/5dd462a573ee6d0014ce715b
def case_check(a, b):
    if a.isalpha() == False or b.isalpha() == False:
        return -1
    elif a.isupper() == b.isupper():
        return 1
    else:
        return 0
