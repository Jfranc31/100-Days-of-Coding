import random
from art import logo, vs
from game_data import data
from os import system


def info_1(person):
    print(f"Compare A: {person['name']}, a {person['description']}, from {person['country']}.")


def info_2(person):
    print(f"against B: {person['name']}, a {person['description']}, from {person['country']}.")


def check_b(a):
    b = random.choice(data)
    while a == b:
        b = random.choice(data)
    return b


def continue_game(a):
    print(logo)
    print(f"You're right! Current score: {final_score}.")
    info_1(a)
    print(vs)
    b = check_b(a)
    info_2(b)
    check_followers(a, b)


def end_game():
    system('clear')
    print(logo)
    print(f"Sorry, that's wrong. Final score: {final_score}")


def check_followers(a, b):
    global final_score
    choice = input("Who has more followers? Type 'A' or 'B': ").lower()
    if choice == 'A':
        if a['follower_count'] > b['follower_count']:
            final_score += 1
            system('clear')
            continue_game(a)
        else:
            end_game()
    else:
        if compare_A['follower_count'] < compare_B['follower_count']:
            final_score += 1
            system('clear')
            continue_game(b)
        else:
            end_game()


# Begin Game
final_score = 0
print(logo)
compare_A = random.choice(data)
info_1(compare_A)
print(vs)
compare_B = check_b(compare_A)
info_2(compare_B)
check_followers(compare_A, compare_B)
