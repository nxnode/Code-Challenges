# https://www.codewars.com/kata/5dd462a573ee6d0014ce715b
def case_check(a, b):
    case_result = 2
    if isinstance(a, str) == True:
        if a.isupper() == b.isupper():
            return case_result == 1
        else:
            return case_result == 0
    else:
        return case_result == -1
