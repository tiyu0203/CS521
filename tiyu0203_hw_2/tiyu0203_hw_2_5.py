"""
Tiffany Yu
Class: CS 521 - Fall 2
Date: 11/12/21
Homework Problem #2_5
Description of Problem: 
Print out a specific word/phrase depending 
on if the number is divisible by a specific number. 
"""

MAXVAL = 30

i = 0
for i in range(MAXVAL):
    i += 1
    if (i % 30 == 0):
        print(i,":foobarbaz\n")
    elif (i % 15 == 0):
        print(i,":barbaz\n")
    elif (i % 10 == 0):
        print(i,":foobaz\n")
    elif (i % 6 == 0):
        print(i,":foobar\n")
    elif (i % 2 == 0):
        print(i,":foo\n")
    elif (i % 3 == 0):
        print(i,":bar\n")
    elif (i % 5 == 0):
        print(i,":baz\n")
    else:
        print(i,":\n")