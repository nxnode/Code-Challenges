# https://www.codewars.com/kata/5629db57620258aa9d000014


def create_freq_maps(string_one, string_two):
    freq_of_chars1 = {}
    freq_of_chars2 = {}

    for char in string_one:
        if char.islower():
            freq_of_chars1[char] = freq_of_chars1.get(char, 0) + 1
    for char in string_two:
        if char.islower():
            freq_of_chars2[char] = freq_of_chars2.get(char, 0) + 1
    return freq_of_chars1, freq_of_chars2


def find_string_differences(str1, str2):

    freq_of_chars1, freq_of_chars2 = create_freq_maps(str1, str2)

    all_chars = set(
        [key for key in freq_of_chars1 if freq_of_chars1[key] > 1]
        + [key for key in freq_of_chars2 if freq_of_chars2[key] > 1]
    )
    combined_chars = []
    for char in all_chars:
        if freq_of_chars1.get(char, 0) > freq_of_chars2.get(char, 0):
            combined_chars.append(("1", char, freq_of_chars1[char]))
        elif freq_of_chars1.get(char, 0) < freq_of_chars2.get(char, 0):
            combined_chars.append(("2", char, freq_of_chars2[char]))
        else:
            combined_chars.append(("=", char, freq_of_chars1[char]))

    final_chars = [f"{tup[0]}:{tup[1] * tup[2]}" for tup in combined_chars]
    final_chars = sorted(final_chars)
    final_chars = sorted(final_chars, key=len, reverse=True)
    final_chars = "/".join(final_chars)

    return final_chars
