"""
Date: 12/1/21
Final Project
Description of Problem: 
"""

from classes import User, Dinner


if __name__ == "__main__":
    username = "Tiffany"
    user = User(username)
    dinner = Dinner(username, "1")
    print(dinner.__str__())
    dinner.which_choice()
    dinner.add_meal("Rice")
    dinner.enter_meal_file()
    new = "Tiffany"
    assert User(new).check_user() == False, "User already exists"
