"""
Tiffany Yu
Class: CS 521 - Fall 2
Date: 11/30/21
Homework Problem #5_1
Description of Problem: 
Read in a file and see which words occur exactly TWICE in the file
"""
import os
import string 

def list_to_twice_words(word_list):
    unique = set(word_list)
    duplicate = list()
    for word in unique:
        if word_list.count(word) == 2:
            duplicate.append(word)
    return duplicate

while(True):
    filename = input("Enter a text file: ")
    if (os.path.exists(filename)):
        input_file = open(filename)
        contents = input_file.read()
        words = contents.split()
        input_file.close()
        no_punc = list()
        for word in words:
            for letter in string.punctuation:
                word = word.replace(letter, "")
            no_punc.append(word)
        duplicates = list_to_twice_words(no_punc)
        print("The duplicate words in this file are:", duplicates)
        break
    else:
        print("Error: The file", filename, "does not exist in this directory")