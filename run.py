# Your code goes here.
# You can delete these comments, but do not change the name of this file
# Write your code to expect a terminal of 80 characters wide and 24 rows high

import time
from art import *
tprint("Pirate Attack",font="cola",chr_ignore=True)

print('Welcome to Pirate Attack, the Game!\n')

user_name = input("Please enter your Name Commander:")
# The strip() method ensures that something has to be entered and the isalpha() method ensures that no numbers are entered 
while not user_name.strip() or not user_name.isalpha():
    print("The text field must not be left blank and only letters are permitted!")
    user_name = input("Please enter your Name Commander:")
