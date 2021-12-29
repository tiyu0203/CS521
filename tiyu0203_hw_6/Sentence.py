"""
Tiffany Yu
Class: CS 521 - Fall 2
Date: 12/7/21
Homework Problem #6
Description of Problem: 
Create a class that takes in a sentence and strips the punctuation, can get all the words, can get a single word,
can set a word at a specific index, scramble the sentence, and just return the sentence
"""
import string
import random 

class Sentence():
    def __init__(self, sentence=str()):
        words = sentence.split()
        no_punc = list()
        for word in words:
            for letter in string.punctuation:
                word = word.replace(letter, "")
            no_punc.append(word)
        self.__s = no_punc

    def get_all_words(self):
        return self.__s

    def get_word(self, index):
        if index < len(self.__s):
            return self.__s[index]
        else:
            return str()
    
    def set_word(self, index, new_word):
          if index < len(self.__s):
            self.__s[index] = new_word    
        
    def scramble(self):
        return random.sample(self.__s, len(self.__s))
    
    def __repr__(self):
        string_sentence = ' '.join(str(e) for e in self.__s) + "."
        return string_sentence

if __name__ == "__main__":
    SENTENCE = "WAS IT A RAT I SAW?!"
    test_sentence = Sentence(SENTENCE)
    test_sentence.set_word(2, "helloworld")
    x = test_sentence.get_word(2)
    assert x == "helloworld", "x should be 'helloworld'"
    scrambled = test_sentence.scramble()
    scrambled_sentence = ' '.join(str(e) for e in scrambled)
    print("Sentence unit test successful!")
    print("Original version:", SENTENCE)
    print("Scrambled version:", scrambled_sentence)
    print("Final version:", test_sentence.__repr__())