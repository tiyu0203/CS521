"""
Date: 12/1/21
Unit testing
Description of Problem: 
Shows that the methods work
"""
import sys
sys.path.append(".")

from classes import User, Dinner


if __name__ == "__main__":
    username = "Professor"
    assert User(username).check_user() == False, "User already exists"
    user = User(username)
    user.new_user(username)
    dinner = Dinner(username, "1")
    dinner.enter_meal_file()
    dinner.choose_past_meals()
    dinner.dinner_recommendation()


