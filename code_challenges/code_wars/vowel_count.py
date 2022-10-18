# https://www.codewars.com/kata/54ff3102c1bad923760001f3


def vowel_count(sentence):
    vowels = ["a", "e", "i", "o", "u", "A", "E", "I", "O", "U"]
    char_count = [char for char in sentence if char in vowels]
    return len(char_count)
