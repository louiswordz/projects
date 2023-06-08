# Building an app that generates random numbers 

#importing the necessary library
from random import choice
from string import ascii_lowercase

#Differentiating between vowels and consonants
vowels = "aeiou"
consonants = "bcdfghjklmnpqrstuv"
letters = ascii_lowercase

letter1 = input("Enter your firts name, enter 'v' for vowels, 'c' for consonants, and 'l' for any letter : ")
letter2 = input("Enter your firts name, enter 'v' for vowels, 'c' for consonants, and 'l' for any letter : ")
letter3 = input("Enter your firts name, enter 'v' for vowels, 'c' for consonants, and 'l' for any letter : ")

def generate_name():
    for letter in letters:
        if letter1 == "v":
            input_letter1 = choice(vowels)
        elif letter1 == "c":
            input_letter1= choice(consonants)
        else:
            input_letter1 = letter1
        if letter2 == "v":
            input_letter2 = choice(vowels)
        elif letter2 == "c":
            input_letter2 = choice(consonants)
        else:
            input_letter2 = letter2

        if letter3 == "v":
            input_letter3 = choice(vowels)
        elif letter3 == "c":
            input_letter3 = choice(consonants)
        else:
            input_letter3 = letter3
    return input_letter1 + input_letter2 + input_letter3


for i in range(10):
    print(generate_name())
