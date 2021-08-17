import random

random_number = random.randint(1, 100)
attempts = 10
guessing = True

print("I'm thinking of a number between 1 and 100.")
# print(f"Correct answer: {random_number}")

difficulty = input("Choose a difficulty. 'Easy' or 'Hard': ").lower()
if difficulty == 'hard':
    attempts -= 5


def guess_calculator(user_guess):
    if user_guess < 1 or user_guess > 100:
        return "Please input a number within 100 and 1"
    elif user_guess < random_number:
        return f"That is too low."
    else:
        return f"That's too high"


while attempts != 0:
    print(f"You have {attempts} attempts remaining to guess the number.")
    guess = int(input("Make a guess: "))
    if guess == random_number:
        print(f"The answer was indeed {random_number}")
        break
    else:
        print(guess_calculator(guess))
    attempts -= 1
    if attempts == 0:
        print(f"You've run out guesses, the number was {random_number}")

