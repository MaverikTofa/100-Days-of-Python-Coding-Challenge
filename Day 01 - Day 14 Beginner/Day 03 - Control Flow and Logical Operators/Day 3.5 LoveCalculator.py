'''
test compatibility between two people
to work out the love score between two people:
    - take both people names and check for the number of times the letters in word TRUE occurs.
    - then check for the number of times the letters in the word LOVE occurs.
    - then combine these numbers to make a 2 digit number.

For love score less than 10 or greater than 90 the message should be:
    "Your score is **x**, you go together like coke and mentos."

For Love Scores between 40 and 50, the message should be:
    "Your score is **y**, you are alright together."

Otherwise, the message will just be their score. e.g.:
    "Your score is **z**."
'''

#  Don't change the code below
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
# Don't change the code above

# Write your code below

true = len([1 for letter in name1.lower() if letter in "true"] +
           [1 for letter in name2.lower() if letter in "true"])
love = len([1 for letter in name1.lower() if letter in "love"] +
           [1 for letter in name2.lower() if letter in "love"])

score = int(f"{true}{love}")

if score < 10 or score > 90:
    print(f"Your score is {score}, you go together like coke and mentos.")
elif score >= 40 and score <= 50:
    print(f"Your score is {score}, you are alright together.")
else:
    print(f"Your score is {score}.")
