import random

# ask for password length
length = int(input("Enter the password length: "))

# ask for complexity
print("Choose password complexity:")
print("1 - Easy (Only letters)")
print("2 - Medium (Letters + Numbers)")
print("3 - Strong (Letters + Numbers + Symbols)")
choice = int(input("Enter your choice (1/2/3): "))

# define character sets
letters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
numbers = "0123456789"
symbols = "!@#$%^&*()?"

# select characters based on choice
if choice == 1:
    chars = letters
elif choice == 2:
    chars = letters + numbers
elif choice == 3:
    chars = letters + numbers + symbols
else:
    print("Invalid choice, using Strong by default")
    chars = letters + numbers + symbols

# generate password
password = ""
for i in range(length):
    password = password + random.choice(chars)

# show password
print("Generated Password:", password)
