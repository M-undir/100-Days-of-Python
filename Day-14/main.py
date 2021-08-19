from game_data import data
from art import logo, vs
import random


# Pulls a random dictionary from the list
def random_account():
    return random.choice(data)


# Formats it so it's easier for me to print this info
def format_name(account):
    name = account['name']
    # follower_count = account['follower_count']
    description = account['description']
    country = account['country']
    return f"{name}, a {description}, from {country}"


def compare(followers_a, followers_b, guess, score):
    if followers_a > followers_b and guess == 'A' or followers_b > followers_a and guess == "B":
        score += 1
        return True
    else:
        return False


def game():
    print(logo)
    compare_a = random_account()
    against_b = random_account()
    score = 0
    playing = True

    while playing:

        print(f"Compare A : {format_name(compare_a)} ")
        # print(compare_a["follower_count"])
        print(vs)
        print(f"Compare B : {format_name(against_b)}")

        guess = input("Who has more followers? Type 'A' or 'B': ").upper()
        followers_a = compare_a["follower_count"]
        followers_b = against_b["follower_count"]

        # Function used to check answer and return either true or false (true if correct, false if not)
        result = compare(followers_a, followers_b, guess, score)

        compare_a = against_b
        against_b = random_account()

        print(logo)
        # If function returns false then the game stops and your final score is revealed otherwise you continue
        if result:
            score += 1
            print(f"You're right! Current score: {score}")
        else:
            playing = False
            print(f"Sorry that's wrong. Final score: {score}")


game()
