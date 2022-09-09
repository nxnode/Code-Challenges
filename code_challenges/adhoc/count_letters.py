def count_letters(characters):
    char_amounts = {}
    for char in characters:
        if not char in char_amounts:
            char_amounts[char] = 1
        else:
            char_amounts[char] += 1
        # frequency map

    char_most = ""
    char_most_count = 0

    for char, count in char_amounts.items():
        if count > char_most_count:
            char_most_count = count
            char_most = char
    return char_most
