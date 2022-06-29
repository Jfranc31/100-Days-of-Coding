# ############## Blackjack Project #####################

# Difficulty Normal 😎: Use all Hints below to complete the project.
# Difficulty Hard 🤔: Use only Hints 1, 2, 3 to complete the project.
# Difficulty Extra Hard 😭: Only use Hints 1 & 2 to complete the project.
# Difficulty Expert 🤯: Only use Hint 1 to complete the project.

# ############## Our Blackjack House Rules #####################

# The deck is unlimited in size.
# There are no jokers.
# The Jack/Queen/King all count as 10.
# The Ace can count as 11 or 1.
# Use the following list as the deck of cards:
# cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
# The cards in the list have equal probability of being drawn.
# Cards are not removed from the deck as they are drawn.
# The computer is the dealer.

from os import system
from art import logo
import random

play_game = True
while play_game:
    begin = input("Do you want to play a game of Blackjack? type 'y' or 'n' ")
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    your_hand = []
    your_total = 0
    computer_hand = []
    computer_total = 0
    get_card = True
    if begin == 'y':
        system('clear')
        print(logo)
        your_hand.append(random.choice(cards))
        computer_hand.append(random.choice(cards))
        your_hand.append(random.choice(cards))
        your_total = your_hand[0] + your_hand[1]
        print(f"  Your cards: {your_hand}, current score: {your_total}")
        print(f"  Computer's first card: {computer_hand[0]}")
        while get_card:
            new_card = input("type 'y' to get another card, type 'n' to pass: ")
            if new_card == 'y':
                your_hand.append(random.choice(cards))
                your_total = your_total + your_hand[len(your_hand) - 1]
                if your_total > 21 and 11 in your_hand:
                    your_hand.remove(11)
                    your_hand.append(1)
                    your_total = 0
                    for value in your_hand:
                        your_total += value
                if your_total > 21:
                    get_card = False
                print(f"  Your cards: {your_hand}, current score: {your_total}")
                print(f"  Computer's first card: {computer_hand[0]}")
            else:
                get_card = False
        print(f"  Your final hand: {your_hand}, final score: {your_total}")
        computer_hand.append(random.choice(cards))
        computer_total = computer_hand[0] + computer_hand[1]
        if computer_total <= 16:
            computer_hand.append(random.choice(cards))
            computer_total = computer_total + computer_hand[len(computer_hand) - 1]
        if computer_total > 21 and 11 in computer_hand:
            computer_hand.remove(11)
            computer_hand.append(1)
            computer_total = 0
            for value in computer_hand:
                computer_total += value
        print(f"  Computer's final hand: {computer_hand}, final score: {computer_total}")
        print(len(your_hand))
        if computer_total == your_total:
            print("Draw 🙃")
        elif computer_total == 21 and len(computer_hand) == 2:
            print("You Lose, Opponent has Blackjack 😱")
        elif your_total == 21 and len(your_hand) == 2:
            print("You Win with a Blackjack 😎")
        elif your_total > 21 and computer_total > 21:
            print("You both lose 😤")
        elif computer_total > 21:
            print("Opponent went over. You win 😁")
        elif your_total > 21:
            print("You went over. You lose 😭")
        elif your_total < computer_total:
            print("You lose 😤")
        else:
            print("You Win 😃")
    else:
        play_game = False
