# https://www.codewars.com/kata/54bf1c2cd5b56cc47f0007a1


def count_duplicates(characters):
    freq_of_dupes = {}
    for char in characters.lower():
        freq_of_dupes[char] = freq_of_dupes.get(char, 0) + 1
    duplicate_chars = [char for char, count in freq_of_dupes.items() if count > 1]
    if len(duplicate_chars) == 0:
        return 0

    return len(duplicate_chars)
