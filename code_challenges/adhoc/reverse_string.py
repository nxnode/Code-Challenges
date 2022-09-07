def reverse_string(a_string):
    d = len(a_string)
    result = ''
    for i in range(d):
        result = a_string[i] + result
    return result
