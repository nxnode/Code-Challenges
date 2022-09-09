def count_letters(characters):
    char_amounts = {}
    for char in characters:
        char_amounts[char] = characters.count(char)

    char_most = ""
    char_most_count = 0

    for char in char_amounts:
        if char_amounts[char] > char_most_count:
            char_most_count = char_amounts[char]
            char_most = char
    return char_most


# char_amounts = {'a': 0, 'b': 0,
