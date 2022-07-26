from project_resources.art import logo

print(logo)
print("Welcome to the secret acution program.")


def clear():
    print(chr(27) + '[2j')
    print('\033c')
    print('\x1bc')


bidders = []
running = True

while running:
    name = input("What is your name? ")
    bid = input("What's your bid? $")
    new_bidder = input("Are there any other bidder? Type 'yes' or 'no'.")
    bidder = {}
    bidder["name"] = name
    bidder["bid"] = int(bid)
    bidders.append(bidder)

    if new_bidder == "no":
        running = False
    clear()

winner = ""
winner_bid = 0
for bidder in bidders:
    if bidder["bid"] > winner_bid:
        winner = bidder["name"]
        winner_bid = bidder["bid"]

print(f"The winner is {winner} with a bid of ${winner_bid}")
