'''
Write a program that tells how many days in specific month.
HINT: you will need to know if it is a leap year or not

You are then going to create a function called days_in_month() which will take a year and a month as inputs, e.g.
days_in_month(year=2022, month=2)
And it will use this information to work out the number of days in the month, then return that as the output, eg:28

The List month_days contains the number of days in a month from January to December for a non-leap year. A leap year has 29 days in February.
'''


def is_leap(year):
    leap_or_not = None
    if year % 4 == 0:
        leap_or_not = True
        if year % 100 == 0:
            leap_or_not = False
            if year % 400 == 0:
                leap_or_not = True
    else:
        leap_or_not = False
    return leap_or_not


def days_in_month(year, month):
    month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    ind = month - 1
    if is_leap(year) and month == 2:
        return 29
    return month_days[ind]


#Do NOT change any of the code below
year = int(input("Enter a year: "))
month = int(input("Enter a month: "))
days = days_in_month(year, month)
print(days)
