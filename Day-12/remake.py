import random

attempts = 10
# guessing = True


# print(f"Correct answer: {random_number}")

# difficulty = input("Choose a difficulty. 'Easy' or 'Hard': ").lower()
# if difficulty == 'hard':
#     attempts -= 5

# Checks whether the guess is correct


def guess_calculator(user_guess, random_number, user_turns):
    if user_guess < 1 or user_guess > 100:
        print("Please input a number within 1 and 100")
        return user_turns - 1
    elif user_guess < random_number:
        print(f"That's too low.")
        return user_turns - 1
    elif user_guess > random_number:
        print(f"That's too high")
        return user_turns - 1
    else:
        print(f"Yes! The answer was indeed {random_number}")


def difficulty_setter():
    difficulty_level = input("Choose a difficulty. 'Easy' or 'Hard': ").lower()
    if difficulty_level == 'hard':
        return attempts - 5
    return attempts


def guessing_game():
    answer = random.randint(1, 100)
    turns = difficulty_setter()
    guess = 0

    print("I'm thinking of a number between 1 and 100.")

    while guess != answer:
        print(f"You have {turns} attempts remaining to guess the number.")
        guess = int(input("Make a guess: "))

        turns = guess_calculator(guess, answer, turns)
        if turns == 0:
            print(f"You've run out guesses, the number was {answer}")
            return
        elif guess != answer:
            print("Guess again: ")


guessing_game()
