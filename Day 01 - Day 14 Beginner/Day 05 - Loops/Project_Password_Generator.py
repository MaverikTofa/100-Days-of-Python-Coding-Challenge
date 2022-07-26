import random

from click import password_option

letters = [
    'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o',
    'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D',
    'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S',
    'T', 'U', 'V', 'W', 'X', 'Y', 'Z'
]
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters = int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

#Eazy Level - Order not randomised:
#e.g. 4 letter, 2 symbol, 2 number = JduE&!91

ezy_password = ""

for letter in range(nr_letters):
    ezy_password += random.choice(letters)

for symbol in range(nr_symbols):
    ezy_password += random.choice(symbols)

for number in range(nr_numbers):
    ezy_password += random.choice(numbers)

print(f"Eazy Level password: {ezy_password}")

#Hard Level - Order of characters randomised:
#e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P

hrd_password = ""

password_len = nr_letters + nr_numbers + nr_symbols

choices = ["l", "n", "s"]

while len(hrd_password) != password_len:
    c = random.choice(choices)
    if c == "l":
        hrd_password += random.choice(letters)
        nr_letters -= 1
        if nr_letters == 0:
            choices.remove("l")
    elif c == "n":
        hrd_password += random.choice(numbers)
        nr_numbers -= 1
        if nr_numbers == 0:
            choices.remove("n")
    else:
        hrd_password += random.choice(symbols)
        nr_symbols -= 1
        if nr_symbols == 0:
            choices.remove("s")

print(f"Hard Level password: {hrd_password}")