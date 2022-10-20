# https://www.codewars.com/kata/5264d2b162488dc400000001


def reverse_larger_strings(sentence):
    sentence = sentence.split()
    reversed_words = ""
    for word in sentence:
        if len(word) < 5:
            reversed_words += f"{word} "
        else:
            reversed_word = ""
            for letter in word:
                reversed_word = letter + reversed_word
            reversed_words += reversed_word + " "
    return reversed_words.strip()
