# https://www.codewars.com/kata/54b42f9314d9229fd6000d9c/train/python


def duplicate_encode(word):
    word = word.lower()
    freq = {}
    encoded_word = ""
    for letter in word:
        if letter in freq:
            freq[letter] = ")"
        else:
            freq[letter] = "("
    for letter in word:
        encoded_word += freq[letter]

    return encoded_word
