"""
Tiffany Yu
Class: CS 521 - Fall 2
Date: 11/30/21
Homework Problem #5_1
Description of Problem: 
Create two functions that calculate the factorial of the inputted integer,
one using recursion and the other without. 
"""
def factorial(x):
    x = int(x)
    if x == 1:
        return 1
    else:
        return (x * factorial(x-1))

def factorial2(x):
    x = int(x)
    prod = 1
    while(True):
        if x == 0:
            return prod * 1
            break
        else: 
            if x > 0:
                prod = prod * x
                x = x-1


while(True):
    num = input("Please enter a factorial starting integer: ")
    if num.isnumeric():
        recursion = factorial(num)
        not_recursion = factorial2(num)
        recursion = "{:,}".format(recursion)
        not_recursion = "{:,}".format(not_recursion)
        print("The factorial of", num, "using recursion is:", recursion)
        print("The factorial of", num, "without recursion is:", not_recursion)
        break
    else: 
        print("Error: This is not an integer. Please re-enter.")

