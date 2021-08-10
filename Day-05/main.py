import random
from data import *

print("Welcome to the PyPassword Generator!")
nr_letters = int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

password = ""
for letter in range(nr_letters):
    password += random.choice(letters)

for symbol in range(nr_symbols):
    password += random.choice(symbols)

for number in range(nr_numbers):
    password += random.choice(numbers)

# print(password)
random_password = ''.join(random.sample(password, len(password)))
# randomises the whole password if the exact len is specified
print(random_password)
