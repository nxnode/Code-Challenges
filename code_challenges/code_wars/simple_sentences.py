# https://www.codewars.com/kata/5297bf69649be865e6000922/train/python


def simple_sentences(words):
    punctuation = [".", ",", "?", "!"]
    previous_word = ""
    sentence = ""
    amount_of_words = len(words)
    for i, sentence_parts in enumerate(words):
        if i == 0:
            sentence += sentence_parts
            i += 1
        else:
            if sentence_parts in punctuation:
                if sentence_parts == previous_word and i != amount_of_words:
                    previous_word = sentence_parts
                    i += 1
                else:
                    if i != amount_of_words:
                        sentence = sentence + sentence_parts
                        previous_word = sentence_parts
                        i += 1
            else:
                sentence += " " + sentence_parts
                previous_word = sentence_parts
                i += 1
        if i == amount_of_words and previous_word not in punctuation:
            sentence = sentence + "."
    return sentence
