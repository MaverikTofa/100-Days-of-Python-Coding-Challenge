"""
Write a program which will select a random name from a list of names. The person selected will have to pay for everybody's food bill.

Important: You are not allowed to use the choice() function.

Line 8 splits the string names_string into individual names and puts them inside a List called names. For this to work, you must enter all the names as name followed by comma then space. e.g. name, name, name
"""

import random

# Split string method
names_string = input("Give me everybody's name, seperated by a comma. ")

names = names_string.split(",")
# Don't change the code above

# Write your code below

max_range = len(names) - 1
unlucky = random.randint(0, max_range)
who_pays = names[unlucky]

print(f"person who will pay: {who_pays}")
