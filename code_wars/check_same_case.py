# https://www.codewars.com/kata/5dd462a573ee6d0014ce715b
def same_case(a, b):
    case_result = 2
    if isinstance(a, str) == True:
        if a.isupper() == True and a.isupper() == b.isupper():
            return case_result == 1
            if a.isupper() == False and a.isupper() == b.isupper():
                return case_result == 0
        else:
            return case_result == -1
