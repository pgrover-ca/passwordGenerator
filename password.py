# Create a password generator that generates secure passwords 
# min length 12 characters and can be used to generate longer lengths. Take input from user. Max length 32 characters
# Must contain letters, numbers and special characters. Letters to contain both upper and lower case
# Only to include Special Characters from this list - [#@!$%^&*-+=_]

import string
import secrets
import random

def randomize_string(input_string):
    # Convert the string to a list of characters
    char_list = list(input_string)
    # Shuffle the characters randomly
    random.shuffle(char_list)
    # Convert the shuffled list back to a string
    randomized_string = ''.join(char_list)
    return randomized_string

def contains_special_character(input_string):
    special_characters = "#@!$%^&*-+=_"
    for char in input_string:
        if char in special_characters:
            return True
    return False

def generate_password(number):
    special_char = "#@!$%^&*-+=_"
    alphabet = string.ascii_letters + string.digits + special_char
    password = ''.join(secrets.choice(alphabet) for i in range(number))
    if contains_special_character(password):
        secure_password = randomize_string(password)
        return secure_password
    else:
        return generate_password(number)

passwd_length = input("Please enter password length (min 12 | max 32): ")

if passwd_length.isdigit():
    number = int(passwd_length)
    if 12 <= number <= 32:
        secure_password = generate_password(number)
        print(secure_password)
    else:
        print("Invalid input. Please enter a valid integer between 12 and 32.")
else:
    print("Invalid input. Please enter a valid integer between 12 and 32.")


