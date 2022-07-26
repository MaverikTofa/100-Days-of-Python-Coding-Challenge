"""
Write a Program that takes the user input for first and a second number and an operator to calculate a result and then asks the user if it should continue doing  calculation based on the last result or start fresh
"""


def first_calc():
    num1 = input("What's the first number?: ")
    operation = input("+\n-\n*\n/\nPick an operation: ")
    num2 = input("What's the second number?: ")
    result = eval(f"{num1}{operation}{num2}")
    print(f"{num1} {operation} {num2} = {result}")
    return result


def next_calc(previous_calc):
    operation = input("+\n-\n*\n/\nPick an operation: ")
    num2 = input("What's the second number?: ")
    result = eval(f"{previous_calc}{operation}{num2}")
    print(f"{previous_calc} {operation} {num2} = {result}")
    return result


while True:
    previous_calc = first_calc()
    continue_calc = input(
        f"Type 'y' to continue calculating with {previous_calc}, or type 'n' to start a new calculation: "
    )
    keep_calc = True
    while keep_calc:
        previous_calc = next_calc(previous_calc)
        continue_calc = input(
            f"Type 'y' to continue calculating with {previous_calc}, or type 'n' to start a new calculation: "
        )
        if continue_calc == 'n':
            keep_calc = False
