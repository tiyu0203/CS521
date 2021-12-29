"""
Tiffany Yu
Class: CS 521 - Fall 2
Date: 11/30/21
Homework Problem #5_1
Description of Problem: 
Prompt the user for 4 numbers seperated by a specific delimeter.
Check for any errors to make sure it's 4 numbers seperated by that delimeter and calculate
the specific formula
"""
while(True):
    num_string = input("Please enter 4 numbers seperated by commas (ie. 1, 3, 4, 5): ")
    if ',' in num_string:
        numbers = num_string.split(',')
        if (len(numbers) > 4):
            print("Error: Too many numbers input")
        else:
            try:
                result = ((float(numbers[0]) * float(numbers[1])) + float(numbers[2]))/float(numbers[3])
                print("((",float(numbers[0]), "*", float(numbers[1]), ") +",float(numbers[2]),") /", float(numbers[3]), "=", result)
                break
            except ZeroDivisionError as e:
                print("ERROR : "+str(e))
            except IndexError as e:
                print("ERROR : "+str(e))
            except ValueError as e:
                print("ERROR : "+str(e))

    else:
        print("Error: Wrong delimeter. Use a comma!")
