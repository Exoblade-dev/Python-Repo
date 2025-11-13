# we would ask the user for preferences
# -length
# -uppercase
# -special symbols
# -digits

# get aall possible chaaracters
# ranndomly pick the characters
# ensure that we have atleast one of each type
# check if the length of the password is valid 


import random 
import string

def generate_password():
    length = int(input("Enter the length of the password: ").strip())
    include_uppercase = input("Do you want to include uppercase letters? (yes/no): ").strip().lower()
    include_special = input("Do you want to include special characters? (yes/no): ").strip().lower()
    include_digit = input("Do you want to include digits? (yes/no): ").strip().lower()
    
    
    if length < 4 :
        print("Length of the password should be at least 4 characters.")
        return
    
    lower = string.ascii_lowercase
    upper = string.ascii_uppercase if include_uppercase == "yes" else ""
    special = string.punctuation if include_special == "yes" else ""
    digit = string.digits if include_digit == "yes" else ""
    all_characters = lower + upper + special + digit 
    
    required_characters = []
    if include_uppercase == 'yes':
        required_characters.append(random.choice(upper))
    if include_special == 'yes':
        required_characters.append(random.choice(special))
    if include_digit== 'yes':
        required_characters.append(random.choice(digit))
        
    remaining_length = length - len(required_characters)
    password = required_characters
    
    for _ in range (remaining_length):
        character = random.choice(all_characters)
        password.append(character)
        
    random.shuffle(password)
    
    final_password = "".join(password)
    
    print(final_password)
    
generate_password()
    
    
    