# https://www.codewars.com/kata/5a19226646d843de9000007d/train/python

def count_consonants(test_string):
    vowels = ("a", "e", "i", "o", "u")
    consonants = set(letter for letter in test_string.lower() if letter not in vowels and letter.isalpha())
    return len(consonants)
