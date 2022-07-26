'''
Pizza Order
Write a program based on the user's order, work out their finall bill.

    - Small Pizza: $15
    - Medium Pizza: $20
    - Large Pizza: $25
    - Pepperoni for small Pizza: +$2
    - Pepperoni for medium or large Pizza: + $3
    - Extra cheese for any size Pizza: + $1
'''

# Don't change the code below
from operator import add


print("Welcome to Python Pizza Deliveries!")
size = input("What Size Pizza do you want? S, M or L ")
add_Pepperoni = input("Do you want pepperoni? Y or N ")
extra_cheese = input("Do you want extra cheese? Y or N ")
# Don't change the code above

# Write your code below

total = 0

if size == "S":
    total = 15
elif size == "M":
    total = 20
else:
    total = 25

if add_Pepperoni == "Y" and size == "S":
    total += 2
elif add_Pepperoni == "Y" and (size == "M" or size == "L"):
    total += 3

if extra_cheese == "Y":
    total += 1

print(f"Your final bill is ${total}")
