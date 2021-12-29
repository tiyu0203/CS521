"""
Tiffany Yu
Class: CS 521 - Fall 2
Date: 11/20/21
Homework Problem #3_5
Description of Problem: 
Read a file that contains student records in each line.
Save each line as a tuple in a list and print them out as student records.
"""
import os

INPUTFILENAME = "cs521_3_5_input.txt"

if (os.path.exists(INPUTFILENAME)):
    input_file = open(INPUTFILENAME, 'r')
    lines = input_file.readlines()
    input_file.close()
    data = [tuple(line[:-1].split(", ")) for line in lines]
    print("Student Records:", data)

else:
    print("Error: The file", INPUTFILENAME, "does not exist in this directory")

