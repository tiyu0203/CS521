"""
Tiffany Yu
Class: CS 521 - Fall 2
Date: 12/1/21
Final Project
Description of Problem: 
"""

import os
import random 

class User():
    '''This class constructs the User Object and its contents. 
    It makes sure the user exists, and opens a new file for a new user '''
    def __init__(self, user=str()):
        self.__user = user

    def check_user(self):
        #check if the user exists aleady
        if (os.path.exists(self.__user)): 
            return True
        else:
            return False

    def new_user(self, user=str()):
        #creates a new file for a new user
        user_file = open(user, "x")

    def user_stats(self):
        #prompts the user to make a choice in what they would like to do in the program 
        print("1 - Type and log in most recent dinner meal")
        print("2 - Print out past dinner meals and choose one of those")
        print("3 - Enter and log in a file that contains a list of dinner meals")
        print("4 - Give me a dinner meal recommendation")
        print("5 - Exit the program")
        choice = input("What would you like to do? Please enter one of the following [1, 2, 3, 4, 5]: ")
        return choice
    

class Dinner():
    '''This class constructs the Dinner Object and its contents.
    The class processes the user's choice and adds to the dinner diary depending on what the user wants. '''
    def __init__(self, user=str(), dinner_option=str()):
        self.user = user
        self.option = dinner_option

    def __repeat(self):
        #reprompts the user incase they want to choose another option 
        choice = User.user_stats(self)
        dinner = Dinner(self.user, choice)
        dinner.which_choice()

    def add_meal(self, dinner = str()):
        #helper function that opens the file and adds a meal to the user's file
        file = open(self.user, "a")        
        file.write(dinner + "\n")
        file.close()

    def single_meal(self):
        #adds a single meal to the user's file
        dinner = input("Please enter your latest dinner meal (for example, spaghetti): ")
        self.add_meal(dinner)

    def unique_meals(self):
        #returns all the different unique meals that the user has ever logged in 
        file = open(self.user)
        meals = file.read().splitlines()
        file.close()
        unique_meals = set(meals)
        return unique_meals

    def choose_past_meals(self):
        #prints out the past meals indexed for the user to choose from 
        unique_meals_list = self.unique_meals()
        index = list(range(1,len(unique_meals_list)+1))
        index_meals = dict(zip(index, unique_meals_list))
        print(index_meals)
        chosen_meal = input("Please type the number corresponding to the meal you want to add: ")
        try:
            #user can choose the meal by entering the corresponding number
            if int(chosen_meal) not in index:
                print("You did not enter a valid number, try again")
                self.choose_past_meals()

            for key, val in index_meals.items(): 
                if key == int(chosen_meal):
                    self.add_meal(val)
        #throws an error if anything but a number is entered
        except ValueError as e:
            print("ERROR : "+str(e))

    def enter_meal_file(self):
        #takes in a file and will read the meals and add it to the user's file
        print("In the text file, each meal should be on a seperate line, otherwise the meals will not be logged in correctly")
        #holds the user accountable if they do not input a file that is formatted correctly
        filename = input("Please enter a text file: ")
        file = open(filename)
        #check if the file exists
        if (os.path.exists(filename)):
            meals = file.read().splitlines()
            for meal in meals:
                self.add_meal(meal)
            file.close()
        else:
            print("Error: The file", filename, "does not exist in this directory")
            self.enter_meal_file()

    def __sizeof__(self, x):
        #get's the length of whatever is input
        return len(x)

    def dinner_recommendation(self):
        #will give a dinner recommendation to the user
        print("Dinner Diary can help recommend a meal if you're stuck!")
        print("We won't recommend a meal you've eaten in the last # days")
        num = input("Please enter the limit as a whole number: ")
        #checking to see the input is a number
        if num.isnumeric():
            input_num = int(num)
            file = open(self.user)
            meals = list(file.read().splitlines())
            #gets all the meals
            last_meals = meals[-input_num:]
            #gets all the meals eaten in the last x amount of days
            all_meals = self.unique_meals()
            for meal in last_meals:
                if meal in all_meals:
                    all_meals.remove(meal)
                    #removes the meals eaten in the last x amount of days
            if self.__sizeof__(all_meals) == 0:
                # if there is not enough meals to choose from - after the meals from the last x amount of days are removed,
                #the usuer will be prompted to enter a lower number
                print("Sorry, you don't have enough variety to get a recommendation")
                print("Try a lower limit number")
                self.dinner_recommendation()
            else:
                #a random meal from the remaining meals is then chosen
                all_meals = tuple(all_meals)
                recommendation = random.choice(all_meals)
                print("Our recommendation based on your past meals is:", recommendation)	
        else:
            print("You did not enter a number. Try again")
            self.dinner_recommendation()

    def which_choice(self):
        #calls the method to perform the task depending on what the user chooses
        if self.option == "1":
            self.single_meal()
            self.__repeat()
        elif self.option == "2":
            self.choose_past_meals()
            self.__repeat()
        elif self.option == "3":
            self.enter_meal_file()
            self.__repeat()
        elif self.option == "4":
            self.dinner_recommendation()
            self.__repeat()
        elif self.option == "5":
            pass
        else:
            print("Invalid Entry, Try again ")
            self.__repeat()

    def __str__(self):
        #returns a general summary statement for the user
        uniqe_meal_list = ', '.join(str(e) for e in self.unique_meals())
        return "Hello " + self.user + "! Your past meals are: " + uniqe_meal_list