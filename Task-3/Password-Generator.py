import random

length = int(input("Enter the desired password length: "
letters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
numbers = "0123456789"
symbols = "!@#$%^&*()_-+=<>?/"

characters = letters + numbers + symbols

password = ""

for i in range(length):
    password = password + random.choice(characters)

print("Generated Password:", password)
