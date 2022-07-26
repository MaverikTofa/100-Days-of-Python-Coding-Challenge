'''
Prime numbers are numbers that can only be cleanly divided by itself and 1.

You need to write a function that checks whether if the number passed into it is a prime number or not.

e.g. 2 is a prime number because it's only divisible by 1 and 2.

But 4 is not a prime number because you can divide it by 1, 2 or 4.
'''


#Write your code below
def prime_checker(number):
    if number > 2 and number % 2 == 0:
        return f"{number} is not a prime number."
    else:
        for i in range(3, number, 2):
            if number % i == 0:
                return f"{number} is not a prime number."
    return f"{number} is a prime number."


#Do NOT change any of the code below
n = int(input("Check this number: "))
print(prime_checker(number=n))
