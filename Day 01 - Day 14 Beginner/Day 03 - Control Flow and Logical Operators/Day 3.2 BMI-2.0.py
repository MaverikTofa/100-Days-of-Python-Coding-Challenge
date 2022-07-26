'''
Write a program that interprets the Body Mass Index (BMI) based on a user weight and height.
it should output the interpretation of their BMI based on BMI value.
    - Under 18.5 they are underweight
    - over 18.5 but below 25 they are normal weight
    - over 25 but below 30 they are overweight
    - over 30 but below 35 they are obese
    - above 35 they are clinically obese
'''

# Don't change the code below
height = float(input("enter your height in m: "))
weight = float(input("enter your weight in kg: "))
# Don't change the code above

# Write your code below

bmi = round(weight / height**2)
print(f"Your BMI {bmi}")

if bmi > 35:
    print("You are Clinically Obese")
elif bmi > 30:
    print("You are Obese")
elif bmi > 25:
    print("You are Overweight")
elif bmi > 18.5:
    print("You are Normal Weight")
else:
    print("You are Underweight")
