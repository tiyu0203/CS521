"""
Tiffany Yu
Class: CS 521 - Fall 2
Date: 11/12/21
Homework Problem #2_3
Description of Problem: 
Prompt the user to enter a number and compute a specific formula. 
Print out the formula as well as the calculated value. 
"""

part_a = input("Please enter a number: ")

n = int(part_a)
part_b = (n**3) / n


print(part_a + "**3 / " + part_a + " = " + str(part_b))