"""
Tiffany Yu
Class: CS 521 - Fall 2
Date: 11/12/21
Homework Problem #2_1
Description of Problem: 
Prompt the user to input a whole number from a specific range. 
Perform a series of calculations and conversions with the input 
number then print the result out.
"""

part_a = input("Please enter a whole number from 1 to 7: ")

part_b = (((int(part_a) * 2) + 10) /2) - int(part_a)

print("The result of part b's calculation as an integer: ", int(part_b))

part_d = int(part_a)*100 + ((int(part_a) + 1) *10) + (int(part_a)+2)

part_e = 0
for digit in str(part_d):
    part_e += int(digit)
print("The sum of the three-digit version of the inputted number: ", part_e)

part_f = part_d/part_e
print("Part d / Part e as a float: ", float(part_f))

print("Part d / Part e as a truncated integer: ",int(part_f))
