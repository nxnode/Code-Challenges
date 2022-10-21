# https://www.codewars.com/kata/520b9d2ad5c005041100000f


def pig_latinify(sentence):
    sentence = sentence.split()
    pig_latin_sentence = ""
    for word in sentence:
        if word.isalpha():
            if len(word) < 2:
                pig_latin_sentence += word[0:] + "ay "
            else:
                pig_latin_sentence += word[1:] + word[0] + "ay "
        else:
            pig_latin_sentence += word
    return pig_latin_sentence.rstrip()
