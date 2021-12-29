"""
Tiffany Yu
Class: CS 521 - Fall 2
Date: 11/27/21
Homework Problem #4_3
Description of Problem: 
Create two constant lists for first and last names.
Combine them, but make sure the last name list is longer than the first name.
Fill in the firstname list with None if the lastname list is longer. 
"""

FIRSTNAMES = ['Jane', 'John']
LASTNAMES = ['Doe', 'Deer', 'Black']

print("First Names:", FIRSTNAMES)
print("Last Names:", LASTNAMES)

if (len(LASTNAMES) >= len(FIRSTNAMES)):

    while (len(LASTNAMES) > len(FIRSTNAMES)):
        FIRSTNAMES.append(None)

    full_name = dict(zip(LASTNAMES, FIRSTNAMES))

else:
    print("Error: last name list is not the same size or larger than the first name list")

print("Name Dictionary:",full_name)
