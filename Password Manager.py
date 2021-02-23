import os
import time
import random

username_password = []
def cls():
    os.system('cls')

print("Hello. This program is used to securely store and retreive passwords.")
time.sleep(2)

def new_signin():
    desired_function = input("Would you like to sign in to an existing account or create a new account? Enter 'new' or 'old': ").strip().capitalize()
    return desired_function

def intro():
    name = input("What is your name?: ").strip().capitalize()
    cls()
    age = float(input("What is your age, {}?: ".format(name)))
    cls()
    if age <= 13:
        print("You do not possess the necessary number of years in order to utilise this software. Please return when you are older than the age of 13.")
        time.sleep(4)
        exit()
    
    cls()
    new_signin()
    
    if desired_function == "new":
        new_account()
    elif desired_function == "old":
        sign_in()
    else:
        new_signin()

def new_account():
