'''
Write a program that calculates the Body Mass Index (BMI) from a user's weight and height.
the BMI is calculated by dividing a person's weight in kg by the square of their height in m:

BMI = weight/height**2
'''

# Don't change the code below
height = input("enter your height in m: ")
weight = input("enter your weight in kg: ")
# Don't change the code above

bmi = float(weight)/float(height)**2
print(round(bmi))
