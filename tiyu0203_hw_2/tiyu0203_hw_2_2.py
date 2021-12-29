"""
Tiffany Yu
Class: CS 521 - Fall 2
Date: 11/12/21
Homework Problem #2_2
Description of Problem: 
Prompt the user to enter a string or number,
and print out the input as a string, an integer, 
and a floating-point value. 
"""

part_a = input("Please enter a string or a number: ")

print("Input as a string: ", str(part_a))
print("Input as an integer: ", int(part_a))
print("Input as a float: ",float(part_a))


"""The only data type that can be input that will
 print without generating any errors is an integer
When the user is prompted to enter a string or a number, 
that input's data type is a string.You can easily convert 
an string of an integer into a string, integer, and float,
but you cannot do the same with a float or a string. 
You cannot convert a string of characters into an integer/float. 
"""