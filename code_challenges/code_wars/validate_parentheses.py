# https://www.codewars.com/kata/52774a314c2333f0a7000688


def validate_parentheses(characters):
    parentheses_list = ["(", ")"]
    new_chars = [char for char in characters if char in parentheses_list]
    parentheses = {"(": ")"}
    parentheses_stack = []
    for char in new_chars:
        if char in parentheses.keys():
            parentheses_stack.append(char)
        else:
            if parentheses_stack == []:
                return False
            open_parentheses = parentheses_stack.pop()
            # if char != parentheses[open_parentheses]:
            #     return False
    return parentheses_stack == []
