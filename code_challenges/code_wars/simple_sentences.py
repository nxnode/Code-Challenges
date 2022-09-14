# https://www.codewars.com/kata/5297bf69649be865e6000922/train/python


def simple_sentences(words):
    previous_word = ""
    sentence = ""
    amount_of_words = len(words)
    count_of_loops = 1
    for sentence_part in words:
        if sentence_part == "." and previous_word == ".":
            count_of_loops += 1
            previous_word = sentence_part
        elif sentence_part == ".":
            sentence = sentence + sentence_part
            previous_word = sentence_part
            count_of_loops += 1
        elif sentence_part == ",":
            sentence = sentence + sentence_part
            previous_word = sentence_part
            count_of_loops += 1
        elif count_of_loops == amount_of_words and sentence_part != ".":
            sentence += " " + sentence_part + "."
        elif count_of_loops == 1:
            sentence += sentence_part
            count_of_loops += 1
        else:
            sentence += " " + sentence_part
            previous_word = sentence_part
            count_of_loops += 1
    return sentence
