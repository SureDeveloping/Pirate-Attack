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
print()
print(f"Commander {user_name} I have a mission for you from the King!\n"
"Recently, our coastal cities and trade routes have been threatened by a new, dangerous pirate fleet.\n" 
"Your task is to find the fleet and eliminate the threat.\n")
menu_selection = input(f"Comander {user_name}, do you accept the challenge to sink the pirates and play then press P.\n"
"For a detailed briefing on the strength of the pirate fleet and to read the rules, press R. \n"
"If your are to terrified of the pirates and want to quit press Q.")
