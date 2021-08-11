import random

from data import stages, word_list, logo

print(logo)

chosen_word = random.choice(word_list)
# print(chosen_word)

lives = 6

display = []
for i in chosen_word:
    display += "_"

# print(display)

playing = True
while playing:
    user_guess = input("Please guess a letter: ").lower()

    letter_num = 0
    for i in chosen_word:
        if i == user_guess:
            display[letter_num] = user_guess
        letter_num += 1

    print(f"{' '.join(display)}")

    if user_guess not in chosen_word:
        lives -= 1
        if lives == 0:
            print(f"You lose, the word was {chosen_word}.")
            playing = False

    if "_" not in display:
        playing = False
        print("You win!")

    print(stages[lives])





