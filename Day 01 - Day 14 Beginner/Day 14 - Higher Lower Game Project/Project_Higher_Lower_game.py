'''
Make a higher or lower game to be played in terminal
our version is who has more instagram followers.
'''

from random import choice
from Project_resources import art, data


def clear_and_logo():
    print(chr(27) + "[2J")
    print(art.logo)


def make_subject():
    return choice(data.data)


def compare_text(a, b):
    print(f"Compare A: {a['name']}, {a['description']}, from {a['country']}.")
    print(art.vs)
    print(f"Against B: {b['name']}, {b['description']}, from {b['country']}.")


def compare_winner(a, b):
    if a['follower_count'] > b['follower_count']:
        return "A"
    else:
        return "B"


score = 0
first = make_subject()
second = make_subject()
if second == first:
    second = make_subject()
while True:
    clear_and_logo()
    if score != 0:
        print(f"You are right! Current score: {score}.\n")

    compare_text(first, second)
    right_wrong = input(
        "Who has more Instagram followers? Type 'A' or 'B': ").upper()
    if compare_winner(first, second) == right_wrong and right_wrong == 'A':
        score += 1
        second = make_subject()
        while first == second:
            second = make_subject()
    elif compare_winner(first, second) == right_wrong and right_wrong == 'B':
        score += 1
        first = second
        while first == second:
            second = make_subject()
    else:
        clear_and_logo()
        print(f"Sorry, that is wrong. Final score: {score}.\n")
        break
