"""
Tiffany Yu
Class: CS 521 - Fall 2
Date: 12/1/21
Final Project
Description of Problem: 
"""
import sys
sys.path.append(".")

from classes import User, Dinner


def Prompt():
    print("Dinner Diary is a program that helps users keep track of what they ate for dinner!")
    signin = input("Type 1 to Login or 2 to Register: ")
    if signin == "1":
        username = input("Please enter username: ")
        user = User(username)
        if user.check_user():
            print("Welcome back", username)
            choice = user.user_stats()
            dinner = Dinner(username, choice)
            dinner.which_choice()
    elif signin == "2":
        new_user = input("Please enter a username: ")
        user = User(new_user)
        user.new_user(new_user)
        Prompt()
    else: 
        print("Invalid Entry. Try Again")
        Prompt()



if __name__ == "__main__":
    Prompt()