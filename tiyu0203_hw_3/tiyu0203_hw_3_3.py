"""
Tiffany Yu
Class: CS 521 - Fall 2
Date: 11/20/21
Homework Problem #3_3
Description of Problem: 
Prompt the user for a 3 digit ascending ordered integer,
until they input the right number. Check and print an error statement
if it's not a number, too long, has duplicates, or not ascending order. 
"""

while(True):
    prompt = input("Please enter a 3-digit ascending ordered integer: ")
    if (prompt.isnumeric()):
        if (len(prompt) != 3):
            print("--> Error: You did not enter a 3-digit number.")
            continue
        else:
            if ((prompt[0] == prompt[1]) | (prompt[0] == prompt[2]) | (prompt[1] == prompt[2])):
                #checking if the first number is the same as the second or third, 
                # and if the second is the same as the third
                print("--> Error: Your number contains duplication.")
                continue
            if (((int(prompt[0])+1) == int(prompt[1])) & ((int(prompt[1])+1) == int(prompt[2]))):
                #checking to make sure the numbers are ascending order
                print("Number Accepted!")
                break
            else:
                print("--> Error: The digits are not in ascending order. ")
    else:
        print("--> Error: This is not an integer. Please re-enter.")
        continue
