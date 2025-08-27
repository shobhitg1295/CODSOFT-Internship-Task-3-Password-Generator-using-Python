print("Password Generator")

import random

# ask user for length
length = int(input("Enter the desired password length: "))

# make lists of letters, numbers and symbols
letters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
numbers = "0123456789"
symbols = "!@#$%^&*()_-+=<>?/"

# combine all characters
characters = letters + numbers + symbols

# empty password string
password = ""

# loop to add random characters
for i in range(length):
    password = password + random.choice(characters)

# show the password
print("Generated Password:", password)
