# Your code goes here.
# You can delete these comments, but do not change the name of this file
# Write your code to expect a terminal of 80 characters wide and 24 rows high

import time
import os
from art import *
tprint("Pirate Attack",font="cola",chr_ignore=True)

print('Welcome to Pirate Attack, the Game!\n')

user_name = input("Please enter your Name Commander:")
# The strip() method ensures that something has to be entered and the isalpha() method ensures that no numbers are entered 
while not user_name.strip() or not user_name.isalpha():
    print("The text field must not be left blank and only letters are permitted!")
    user_name = input("Please enter your Name Commander:")
print()
print(f"Comander {user_name} I have a mission for you from the King!\n"
"Recently, our coastal cities and trade routes have been threatened by a new, dangerous pirate fleet.\n" 
"Your task is to find the fleet and eliminate the threat.\n")

menu_selection = input(f"Comander {user_name}, do you accept the challenge to sink the pirates and play the game then press P.\n"
"For a detailed briefing on the strength of the pirate fleet and to read the rules, press R. \n"
"If your are to terrified of the pirates and want to quit press Q: ").upper()

def main_menu(menu_selection):
    """
    	The function provides the selection in the main menu. 
        The valid data input is checked and the game is started, 
        terminated or the rules are displayed according to the user input. 
        Before the input is called up, the previous entries in the console are deleted
    """
    os.system('clear')
    if menu_selection == 'R':
        print("A pirate fleet has been spotted off the coast, consisting of: \n"
    	"1 - 1-masted ship - 2 tiles long\n"
        "2 - 2-masted ships - 3 tiles long\n"
        "1 - 3-masted ship - 4 tiles long\n"
        "1 - 4-masted ship - 5 tiles long\n"
        "To sink the ships, select a coordinate that you want to shoot at. \n"
        "If you hit it, this will be indicated by an X in the coordinate system.\n" 
        "If the shot is a miss, the field is marked with an O.\n"
        "Choose your shots carefully. We only have only 25 shells left.\n"
        "These must be enough to defeat the pirates."
        )
    elif menu_selection == 'Q':
        print(f"Thank you Comander {user_name} for playing Pirate Attack!\n"
        "I wish you at all times a hand's width of water under your keel and save travels.\n"
        "See you soon, the next battle is already waiting for you.\n")
    elif  menu_selection == 'P':
        print('P selected')
    else:
        input("Please select P, R or Q. All other entries are not permitted: ").upper()

main_menu(menu_selection)
