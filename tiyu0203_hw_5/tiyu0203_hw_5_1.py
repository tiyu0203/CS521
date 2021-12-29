"""
Tiffany Yu
Class: CS 521 - Fall 2
Date: 11/30/21
Homework Problem #5_1
Description of Problem: 
Take in a file and count how many vowels and consonants are in the words in the text file
"""
import os

VOWELS = ['A', 'E', 'I', 'O', 'U']

def vc_count(filename):
    
    vowel_count = 0
    cons_count = 0

    input_file = open(filename)
    contents = input_file.read()
    words = contents.upper().split()
    for word in words:
        for letter in word:
            if letter.isalpha():
                if letter in VOWELS:
                    vowel_count += 1
                else:
                    cons_count += 1
    input_file.close()

    return {"vowels": vowel_count, "consonants": cons_count}

while(True):
    filename = input("Enter a text file: ")
    if (os.path.exists(filename)):
        letters = vc_count(filename)
        print("Total # of vowels in text file:", "{:,}".format(letters["vowels"]))
        print("Total # of consonants in text file:", "{:,}".format(letters["consonants"]))
        break
    else:
        print("Error: The file", filename, "does not exist in this directory")

