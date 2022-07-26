'''
Create a Guess a number game with easy and hard levels
where hard you get only 5 attempts and 10 on easy
'''
import random


def clear():
    return print(chr(27) + "[2J")


clear()
print("Welcome to the Number Guessing Game!")
print("I'm thinking og a number between 1 and 100.")

secret_number = random.randint(1, 100)

attempts = 10

difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()

if difficulty == "easy":
    print(f"You have {attempts} attempts remaining to guess the number.")
else:
    attempts = 5
    print(f"You have {attempts} attempts remaining to guess the number.")

guess = 0

while guess != secret_number and attempts > 0:
    guess = int(input("Make a guess: "))
    if guess > secret_number:
        attempts -= 1
        print("Too High.\nGuess again.")
        print(f"You have {attempts} attempts remaining to guess the number")
    else:
        attempts -= 1
        print("Too low.\nGuess again.")
        print(f"You have {attempts} attempts remaining to guess the number")

if attempts == 0:
    print("You have run out of guesses, You lose!")
if guess == secret_number:
    print(f"You have got it!!, the secret number is: {secret_number}")