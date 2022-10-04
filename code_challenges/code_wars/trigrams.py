# https://www.codewars.com/kata/55d8dc4c8e629e55dc000068


def extract_trigrams(words):
    if len(words) <= 3:
        return ""
    words = words.replace(" ", "_")
    trigram = ""
    for i in range(len(words) - 2):
        trigram += words[i : i + 3] + " "
    return trigram.strip()
