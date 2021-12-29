"""
Tiffany Yu
Class: CS 521 - Fall 2
Date: 11/20/21
Homework Problem #3_4
Description of Problem: 
Read a specific file with 20 words and output the same words
into another text file with 4 lines of 5 words. 
"""
import os

ALLOWEDWORDS = 20
INPUTFILENAME = "cs521_3_4_input.txt"
OUTPUTFILENAME = "cs521_3_4_output.txt"
WORDSPERLINE = 5

if (os.path.exists(INPUTFILENAME)):

    input_file = open(INPUTFILENAME)
    contents = input_file.read()
    words = contents.split()

    if (len(words) == ALLOWEDWORDS):

        f= open(OUTPUTFILENAME,"w")

        for index in range(0, ALLOWEDWORDS, WORDSPERLINE):

            f= open(OUTPUTFILENAME,"a")
            f.write(' '.join(words[index : index + WORDSPERLINE]) + "\n")

        f.close()
        print("“Success! Output written to:", OUTPUTFILENAME)  
    else:
        print("Error: The file doesn't have 20 words")
else:
    print("Error: The file", INPUTFILENAME, "does not exist in this directory")