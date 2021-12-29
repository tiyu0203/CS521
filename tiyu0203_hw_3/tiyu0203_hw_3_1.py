"""
Tiffany Yu
Class: CS 521 - Fall 2
Date: 11/20/21
Homework Problem #3_1
Description of Problem: 
Loop through a range of numbers,
and count how many are odd, even, squares, and cubes.
"""

BEGINNING = 2
END = 130

odd = 0
even = 0
square = 0
cube = 0

odd_range = []
even_range = []
square_range = []
cube_range = []

for i in range(BEGINNING, END+1):
    if (i % 2 == 0):
        even += 1
        even_range.append(i)

    if (i % 2 == 1):
        odd += 1
        odd_range.append(i)

    if (round(i**(1/3.),2) % 1 == 0):
        #For some reason, some numbers such as 64^(1/3) = 3.999994
        #Which is why I had to round
        cube += 1
        cube_range.append(i)

    if ((i ** (1 / 2)) % 1 == 0):
        square += 1
        square_range.append(i)
  
print("Checking numbers from", BEGINNING, "to", END)
print("Odd (", odd, "):", odd_range[0], "...", odd_range[-1])
print("Even (", even, "):", even_range[0], "...", even_range[-1])
print("Square (", square, "):", square_range)
print("Cube (", cube, "):", cube_range)
