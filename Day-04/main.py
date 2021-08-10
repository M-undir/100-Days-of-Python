import random
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''


game_moves = [rock, paper, scissors]
# print(random.choice(game_moves))
cpu_choice = random.randint(0, 2)
cpu_move = game_moves[cpu_choice]

user_choice = int(input("Choose 0 for Rock, 1 for Paper or 2 for Scissors. "))
if user_choice < 0 or user_choice > 2:
    print("Please input a number between 0 and 2")
else:
    print(game_moves[user_choice])
    print(f"Computer chose:\n {game_moves[cpu_choice]}")
    # print(game_moves[cpu_choice])
    if user_choice == 2 and cpu_choice == 0:
        print("You lose")
    elif user_choice > cpu_choice:
        print("You win")
    elif user_choice == 0 and cpu_choice == 2:
        print("You win")
    elif user_choice < cpu_choice:
        print("You lose")
    else:
        print("It's a draw")
