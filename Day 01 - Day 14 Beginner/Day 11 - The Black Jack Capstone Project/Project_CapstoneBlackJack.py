'''
Create a program to play our version of BLACKJACK
'''

###################################################
'''
#OUR BLACKJACK HOUSE RULES
    - the deck is unlimited in size.
    - there are no jokers.
    - the Jack/Queen/King all count and replaced by 10.
    - the Ace can count as 11 or 1.
    - use the following list as the deck of cards:
        cards = [11,2,3,4,5,6,7,8,9,10,10,10,10]
    - the cards in the list have equal probability if being drawn.
    - cards are not removed from the deck as they are drawn.
'''

import random
from project_resources import art


def deal_card():
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    return random.choice(cards)


def calculate_score(lst):
    if sum(lst) == 21 and len(lst) == 2:
        return 0
    if sum(lst) > 21 and 11 in lst:
        lst.remove(11)
        lst.append(1)
    return sum(lst)


def compare(user_score, computer_score):
    if user_score == computer_score:
        return "Draw :P"
    elif computer_score == 0:
        return "Lose, Computer has Blackjack :("
    elif user_score == 0:
        return "Win with Blackjack :)"
    elif user_score > 21:
        return "You went over. You lose :("
    elif computer_score > 21:
        return "Computer went over. you win :D"
    elif user_score > computer_score:
        return "You win :)"
    else:
        return "You lose :("


def play_game():
    print(art.logo)
    user_cards = [deal_card() for i in range(2)]
    computer_cards = [deal_card() for i in range(2)]

    is_game_over = False

    while not is_game_over:
        user_score = calculate_score(user_cards)
        computer_score = calculate_score(computer_cards)

        print(f"    Your cards: {user_cards}, current score: {user_score}")
        print(f"    Computer's first card: {computer_cards[0]}")

        if user_score == 0 or computer_score == 0 or user_score > 21:
            is_game_over = True
        else:
            user_should_deal = input(
                "Type 'y' to draw another card, or type 'n' to pass: ")
            if user_should_deal == 'y':
                user_cards.append(deal_card())
            else:
                is_game_over = True

    while computer_score != 0 and computer_score < 17:
        computer_cards.append(deal_card())
        computer_score = calculate_score(computer_cards)

    print(f"\n    Your final hand: {user_cards}, final score: {user_score}")
    print(
        f"    computer final hand: {computer_cards}, final score: {computer_score}"
    )
    print(compare(user_score, computer_score))


def clear():
    return print(chr(27) + "[2J")


while input("\nDo you want to play a new game if Blackjack? type 'y' or 'n': "
            ) == "y":
    clear()
    play_game()
