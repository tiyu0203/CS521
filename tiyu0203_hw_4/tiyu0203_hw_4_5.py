"""
Tiffany Yu
Class: CS 521 - Fall 2
Date: 11/27/21
Homework Problem #4_5
Description of Problem: 
Store the text versions of numbers and - and . in a dictionary. 
After entering a number, as long as there are no words or commas,
the text version of the number is printed out. 
"""
NUMBERS = {1: 'One', 2: 'Two', 3: 'Three', 4: 'Four', 5: 'Five', 6: 'Six', 7: 'Seven', 8: 'Eight', 9: 'Nine', 0: 'Zero', '-': 'Negative', '.': 'Point'}
as_text = []

while(True):
    number = input("Enter a number: ")
    if number.isnumeric():
        for n in number:
            as_text.append(NUMBERS[int(n)])
        print("As Text:", ' '.join(as_text))
        break
    if number.lower().islower():
         print('"', number, '"', "is not a valid number. Please try again")
    else:
        if ',' in number:
            print("Please try again without entering commas.")
        else: 

            if '.'or '-' in number:
                for n in number:
                    if n == '.':
                        as_text.append(NUMBERS['.'])
                    elif n == '-':
                        as_text.append(NUMBERS['-'])
                    else:
                        as_text.append(NUMBERS[int(n)])
                print("As Text:", ' '.join(as_text))
                break
           
            