#password generator

import random
import string

def generate_pass(min_length,numbers=True,special_characters=True):
    letters=string.ascii_letters               #contains all letters--> a to z
    digits=string.digits                       #contains all digitss--> 0 to 9
    special=string.punctuation                 #contain common special characters

    characters = letters 

    if numbers :
        characters+=digits
    if special_characters:
        characters+=special 

    pwd=""
    meets_criteria=False
    has_number=False
    has_special=False 

    while not meets_criteria or len(pwd)<min_length:
        new_char = random.choice(characters)
        pwd+=new_char

        if new_char in digits:
            has_number=True 

        elif new_char in special:
            has_special=True 

        meets_criteria=True 
        if numbers:
            meets_criteria=has_number 
        if special_characters:
            meets_criteria = meets_criteria and has_special

    return pwd 
min_length = int(input("Enter the minimum length:"))

while True:
    choice=input("Do you want numbers?\nType:\nY for Yes and\nN for No:").lower()
    if choice in ("y","n"):
        has_number=choice=="y"
        break 
    print("Please enter only Y or N")

while True:
    choice=input("Do you want special character?\nType:\nY for Yes and\nN for No:").lower()
    if choice in ("y","n"):
        has_special=choice=="y"
        break 
    print("Please enter only Y or N")


pwd=generate_pass(min_length,has_number,has_special)
print("The generated password is:",pwd)