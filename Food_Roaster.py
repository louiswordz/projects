from random import choice
from datetime import datetime as dt
import pandas as pd

food_data = pd.read_csv("/Users/leo/Documents/python works/Text Generator Project/food_coded.csv")
food = list(food_data['comfort_food'])
food_choice = input("Enter your favourite meal, Enter c for confused :")

Dinner = ['chocolate', 'chips', 'ice cream',
 'frozen yogurt', 'pizza', 'fast food',
 'Pizza', 'Mac and cheese', 'ice cream',
 'Ice cream', 'chocolate', 'chips',
 'Candy', 'brownies and soda.',
 'Chocolate', 'ice cream', 'french fries', 'pretzels',
 'Ice cream', 'cheeseburgers', 'chips.',
 'Donuts', 'ice cream', 'chips',
 'Mac and cheese', 'chocolate and pasta ',
 'Pasta','macaroni and cheese', 'chicken curry',  'Noodle ( any kinds of noodle)']

Breakfast = ['French fries', 'chicken nuggets','frosted brownies',
 'toast','Lasagna','Ritz','Cheesecake','potato chips and protein bars',
 'mozzarella sticks']

Launch = ['chicken tikka masala and butter naan ', 'Cookies',
 'salty snacks', 'chips', 'candy',
 'Pizza', 'soda', 'chocolate brownie','seaweed soup',
  'Tuna sandwich, and Egg' ]

confused = " "
          
          

def food_menu():
    for diet in food:
        if dt.now() < dt(dt.today(), dt.hour(), 12):
            print("What will you like to have for breakfast?")
        if food_choice == confused:
            breakfast = choice(Breakfast)
        elif food_choice in Breakfast:
            breakfast = Breakfast
        elif food_choice == diet:
            breakfast = diet
        else:
            Breakfast = food_choice


        if  dt.time(12) > dt.now() < dt.time(18):
            print("What will you like to have for Launch?")
        if food_choice == confused:
            launch = choice(Launch)
        elif food_choice in Launch:
            launch = Launch
        elif food_choice == diet:
            launch = diet
        else:
            launch = food_choice


        if dt.now > dt.time(18):
            print("What will you like to have for Dinner?")
        if food_choice == confused:
            dinner = choice(Dinner)
        elif food_choice in Dinner:
            dinner = Launch
        elif food_choice == diet:
            dinner = diet
        else:
            dinner = food_choice

food_menu()



