import random

# ask user for length
length = int(input("Enter the desired password length: "))

# make lists of letters, numbers and symbols
letters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
numbers = "0123456789"
symbols = "!@#$%^&*()_-+=<>?/"

# combine all characters
characters = letters + numbers + symbols
password = ""

for i in range(length):
    password = password + random.choice(characters)

print("Generated Password:", password)

