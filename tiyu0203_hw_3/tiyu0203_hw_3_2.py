"""
Tiffany Yu
Class: CS 521 - Fall 2
Date: 11/20/21
Homework Problem #3_2
Description of Problem: 
Take a docstring with three sentences,
and count how many uppercase, lowercase, digits, and punctuation
in each sentence and print them out in a table. 
"""
import string

DOCSTRING = """Hello, this is homework 3 question 2. 
I am creating 3 sentences for this question. 
This sentence is the third one I need. """

sentence_list = DOCSTRING.split('\n')

upper = 0
lower = 0
digit = 0
punctuation = 0
counter = 0

print("{} {} {} {} {}".format("#", "# Upper", "# Lower", "# Digits", "# Punct."))
print("{} {} {} {} {}".format("-", "-------", "--------", "--------", "--------"))

for sentence in sentence_list:

    for word in sentence:
        for letter in word:
            if letter.isupper():
                upper += 1
            if letter.islower():
                lower += 1
            if letter.isdigit():
                digit += 1
            if letter in string.punctuation:
                punctuation += 1
    counter += 1
    print("{:^} {:^8} {:^7} {:^8} {:^8}".format(counter, upper, lower, digit, punctuation))
    #center the numbers

    upper = 0
    lower = 0
    digit = 0
    punctuation = 0
    #reset the counters when looking at the next sentence 
