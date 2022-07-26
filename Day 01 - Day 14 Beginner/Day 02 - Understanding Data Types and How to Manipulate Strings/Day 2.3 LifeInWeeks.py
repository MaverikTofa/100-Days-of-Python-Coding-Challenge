'''
Create a program using math and f-string that tells us how many days, weeks, months we have left if we live until 90 years old.

it will take current age as an input and output message with our time left in this format
    You have x days, y weeks and z months left.
where x,y and z are replaced with the actual calculated numbers.
'''

# Don't change the code below
age = input("what is your current age? ")
# Don't change the code above

# Write your code below

remaining_years = 90 - int(age)

remaining_months = remaining_years * 12
remaining_weeks = remaining_years * 52
remaining_days = remaining_years * 365

print(
    f"You have {remaining_days} days, {remaining_weeks} weeks and {remaining_months} months left.")
