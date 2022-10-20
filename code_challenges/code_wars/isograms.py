# https://www.codewars.com/kata/54ba84be607a92aa900000f1


def isograms(string):
    eval_string = set(string.lower())
    if len(eval_string) != len(string.strip()):
        return False
    else:
        return True
