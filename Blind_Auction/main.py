from os import system
from art import logo

# HINT: You can call clear() to clear the output in the console.
print(logo)
bidders = []
other_bidder = True
highest_bid = 0


# add bidder
def input_bidder(bidder_name, bidder_bid):
    info = {"bidder": name, "bid": bid}
    bidders.append(info)


# checking for bidders
while other_bidder:
    name = input("What is your name? ")
    bid = int(input("What's your bid? $"))
    input_bidder(name, bid)
    player = input("Is there another bidder? type 'yes' or 'no' ")
    if player == 'yes':
        other_bidder = True
        system('clear')
    else:
        other_bidder = False
        system('clear')

# checking for highest bid and the bidder
for bidder in bidders:
    if highest_bid < bidder["bid"]:
        highest_bid = bidder["bid"]
        highest_bidder = bidder["bidder"]

print(f"The winner is {highest_bidder} with a bid of ${highest_bid}.")