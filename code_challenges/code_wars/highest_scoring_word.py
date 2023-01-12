# https://www.codewars.com/kata/57eb8fcdf670e99d9b000272/train/python


def highest_word(test_string):
    letter_values = {
        "a": 1,
        "b": 2,
        "c": 3,
        "d": 4,
        "e": 5,
        "f": 6,
        "g": 7,
        "h": 8,
        "i": 9,
        "j": 10,
        "k": 11,
        "l": 12,
        "m": 13,
        "n": 14,
        "o": 15,
        "p": 16,
        "q": 17,
        "r": 18,
        "s": 19,
        "t": 20,
        "u": 21,
        "v": 22,
        "w": 23,
        "x": 24,
        "y": 25,
        "z": 26,
    }
    word_list = test_string.split(" ")
    highest_word = ""
    highest_score = 0
    for word in word_list:
        word_score = 0
        for letter in word:
            word_score = word_score + int(letter_values[letter])
        if word_score > highest_score:
            highest_word = word
            highest_score = word_score
    return highest_word
