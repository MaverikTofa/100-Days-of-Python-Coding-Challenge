'''
Write a program that adds the digits in a 2 digit number.
e.g. if the input was 35, then the output should be 10+12=8

Warning. Don't change the code on lines 10-12.
your program should work for different inputs.
e.g. any two-digit number
'''

# Don't change the code below
two_digit_number = input("Type a two digit number: ")
# Don't change the code above

# Write your code below

answer = sum([int(i) for i in str(two_digit_number)])
print(answer)
