"""
Tiffany Yu
Class: CS 521 - Fall 2
Date: 11/27/21
Homework Problem #4_2
Description of Problem: 
Create a string and create a dictionary with the frequency
of each character in alphabetical order. Find the letter(s) that
are most frequent 
"""
import string

SENTENCE = "TACO CAT is a palindrome!"

letter_frequency = {}
freq_letters = []

for i in sorted(SENTENCE.upper()):
    if i.isalpha():
        keys = letter_frequency.keys()
        if i in keys:
            letter_frequency[i] += 1
        else:
            letter_frequency[i] = 1

print("The string being analyzed is:", SENTENCE)
print("1. Dictionary of letter counts:",letter_frequency)

max_value = max(letter_frequency.values())
for key, val in letter_frequency.items(): 
    if val == max_value:
        freq_letters.append(key)

if (len(freq_letters) > 1):
    print("2. Most frequent letters", freq_letters, "appear", max_value, "times.")
else:
    print('2. Most frequent letter "', freq_letters[0], '" appears', max_value, "times.")

