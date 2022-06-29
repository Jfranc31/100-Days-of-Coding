import random
from art import rock, paper, scissors
# Write your code below this line 👇
play_game = True
user_count = 0
computer_count = 0
while play_game:
    print(f"Your score: {user_count} vs. Computer score: {computer_count}")
    user = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))
    computer = random.randint(0, 2)
    if user == 0:
        print(rock)
        print("Computer chose:")
        if computer == 0:
            print(rock)
            print("It is a draw.")
        elif computer == 1:
            print(paper)
            print("You Lose!")
            computer_count += 1
        else:
            print(scissors)
            print("You Won!")
            user_count += 1
    elif user == 1:
        print(paper)
        print("Computer chose:")
        if computer == 0:
            print(rock)
            print("You Win!")
            user_count += 1
        elif computer == 1:
            print(paper)
            print("It is a draw.")
        else:
            print(scissors)
            print("You Lose!")
            computer_count += 1
    else:
        print(scissors)
        print("Computer chose:")
        if computer == 0:
            print(rock)
            print("You Lose!")
            computer_count += 1
        elif computer == 1:
            print(paper)
            print("You Win")
            user_count += 1
        else:
            print(scissors)
            print("It is a draw.")

    if user_count == 2:
        play_game = False
        print("You Won best out of 3!")
    if computer_count == 2:
        play_game = False
        print("Computer Won best out of 3!")
