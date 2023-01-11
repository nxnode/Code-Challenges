# https://www.codewars.com/kata/57eb8fcdf670e99d9b000272/train/python

def highest_word(test_string):
    letter_values = {"a":1
,"b":2,"c":3,"d":4,"e":5,"f":6,"g":7,"h":8,"i":9,"j":10,"k":11,"l":12,"m":13,"n":14,"o":15,"p":16,"q":17,"r":18,"s":19,"t":20,"u":21,"v":22,"w":23,"x":24,"y":25,"z":26}
    summed_words = {}
    word_list = test_string.split(" ")
    for word in word_list:
        summed_words[word] = summed_words.get(word, 0)
        for letter in word:
            summed_words[word] = int(summed_words[word]) + int(letter_values[letter])
    return summed_words