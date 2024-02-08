# Task 3 : Password Generator

# For getting a random character
import random

# Characters used to build the password
characters = "qwertyuioplkjhgfdsazxcvbnmZXCVBNMLKJHGFDSAQWERTYUIOP1234567890!@#$%^&*()-=_+[]{}|;':,./<>"

# Ensure user enters an integer and length of password is between 8-100
while True:
    # Get the password length
    try:
        print()
        password_length = int(input("Enter Password Length: "))
        if(password_length >= 8 and password_length <= 100):
            break
        else:
            print()
            print("Password length must be between 8 and 100")
    # If it is not an integer
    except ValueError:
        print()
        print("Enter an integer!")

# For storing the password
password = ""

# Incrementaly build the password by looping from 0 to Password length - 1
for i in range(password_length):
    # Get the index of a random character
    rand_index = random.randint(0, len(characters)-1)
    # Append the character to the password
    password += characters[rand_index]

# Display the password
print()
print(f"Generated Password = {password}")
print()
