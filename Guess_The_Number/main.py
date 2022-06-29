# Number Guessing Game Objectives:

# Include an ASCII art logo.
# Allow the player to submit a guess for a number between 1 and 100.
# Check user's guess against actual answer. Print "Too high." or "Too low." depending on the user's answer.
# If they got the answer correct, show the actual answer to the player.
# Track the number of turns remaining.
# If they run out of turns, provide feedback to the player.
# Include two different difficulty levels (e.g., 10 guesses in easy mode, only 5 guesses in hard mode).
from art import logo
import random
print(logo)
print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100.")
difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ")
attempts = 0
if difficulty == 'easy':
    attempts = 10
else:
    attempts = 5
answer = random.randint(1, 100)
game_done = False
while not game_done:
    print(f"You have {attempts} remaining to guess the number.")
    guess = int(input("Make a guess: "))
    if guess > answer:
        attempts -= 1
        print("Too high.\nGuess again.")
    elif guess < answer:
        attempts -= 1
        print("Too low.\nGuess again.")
    else:
        print(f"You got it! The answer was {guess}.")
        game_done = True
    if attempts == 0:
        print("You've run out of guesses, you lose.")
        game_done = True
