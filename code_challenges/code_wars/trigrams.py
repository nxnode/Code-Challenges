# https://www.codewars.com/kata/55d8dc4c8e629e55dc000068


def extract_trigrams(words):
    stopping_point = len(words) - 2
    if len(words) <= 3:
        return ""
    spaces_replaced = ""
    for i in words:
        if i == " ":
            i = "_"
        spaces_replaced += i
    words = ""
    for i in range(len(spaces_replaced)):
        words += spaces_replaced[i : i + 3] + " "
        i += 1
        if i == stopping_point:
            return words.strip()
    return words.strip()
