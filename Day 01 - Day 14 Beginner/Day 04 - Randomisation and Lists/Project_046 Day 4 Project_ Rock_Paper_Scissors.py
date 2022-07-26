'''
Make a rock, paper, scissors game.

you'll find the ASCII art for the hand signals already saved to a corresponding variable: rock, paper, and scissors. This will make it easy to print them out to the console.

Start the game by asking the player:

"What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors."

From there you will need to figure out:

How you will store the user's input.
How you will generate a random choice for the computer.
How you will compare the user's and the computer's choice to determine the winner (or a draw).
And also how you will give feedback to the player.
'''

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

#Write your code below

import random

choices = [rock, paper, scissors]

print("Welcome to Rock, Paper, Scissors game\n")

player = input(
    "Plese enter your choice as 0 for Rock, 1 for Paper and 2 for Scissors:  \n"
)

if player in "012":
    player = choices[int(player)]
    computer = random.choice(choices)
    duel = [player, computer]

    print(f"Player{player}   vs\n Computer{computer}")

    winning = [[rock, scissors], [scissors, paper], [paper, rock]]

    if player == computer:
        print("It's a Draw!!\n")
    elif duel in winning:
        print("Player Wins!!\n")
    else:
        print("Comuter Wins!!\n")
else:
    print("Invalid Number, You Lose!!")
