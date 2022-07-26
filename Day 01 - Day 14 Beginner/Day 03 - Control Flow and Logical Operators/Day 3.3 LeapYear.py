'''
Write a program check out if a given year is a leap year.

this is how it works:
    on every year that is evenly divisible by 4
        except every year that is evenly divisible by 100
            unless the year is also evenly divisible by 400
'''

# Don't change the code below
year = int(input("Which year do you want to check? "))
# Don't change the code above

# Write your code below

leap = f"the year {year} is a leap year."
not_leap = f"the year {year} is not a leap year."

leap_or_not = None

if year % 4 == 0:
    leap_or_not = leap
    if year % 100 == 0:
        leap_or_not = not_leap
        if year % 400 == 0:
            leap_or_not = leap
else:
    leap_or_not = not_leap

print(leap_or_not)
