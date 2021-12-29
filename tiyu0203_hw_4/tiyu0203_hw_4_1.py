"""
Tiffany Yu
Class: CS 521 - Fall 2
Date: 11/27/21
Homework Problem #4_1
Description of Problem: 
Create a list of integers and sum the nearest neighbors and itself.
Print the original list and the new list
"""
INTEGERLIST = list(range(55, -5, -10))
#55, 45, 35, 25, 15, 5
LENGTH = len(INTEGERLIST)+2
#To make sure the result list 
#has the same amount of elements
x = 2
RESULTLIST = list()
while (x < LENGTH):
    int_sum = sum(INTEGERLIST[:x])
    RESULTLIST.append(int_sum)
    x += 1

print("Input List: ", INTEGERLIST)
print("Result List: ", RESULTLIST)