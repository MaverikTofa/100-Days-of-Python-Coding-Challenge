'''
Write a program that will get input of the user about how much was the bill value.
also asks the users about how many persons will split the bill.
then it will asks about tip percent you are willing to give.
then output the amount that each person should pay
'''

print("Welcome to the tip calculator!")

bill_value = float(input("What is the total of the bill? $"))
tip_percent = float(
    input("What percentage tip would you like to give? 10, 12, or 15? "))
persons = int(input("How many persons to split the bill? "))

bill_value += bill_value * tip_percent / 100
pay = round(bill_value/persons, 2)

print(f"Each person should pay: ${pay:.2f}")
