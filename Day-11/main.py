# The the Ace can count as 11 or 1.
# Use the following list as the deck of cards:
# cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
# The cards in the list have equal probability of being drawn.
# Cards are not removed from the deck as they are drawn.
# The computer is the dealer.

import random
# from art import logo


def deal_card():
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    card = random.choice(cards)
    return card


def score_calculation(cards):
    if sum(cards) > 21 and 11 in cards:
        cards.remove(11)
        cards.append(1)
    if sum(cards) == 21 and len(cards) == 2:
        return 21
    return sum(cards)


def compare_score(user_score, cpu_score):
    if user_score == cpu_score:
        return "It's a draw"
    elif user_score == 21:
        return "You win with Blackjack"
    elif cpu_score == 21:
        return "Computer wins with Blackjack"
    elif user_score > cpu_score and user_score < 21:
        return "You are closer to 21 so you win!"
    elif user_score < cpu_score and user_score > 21:
        return "You are closer to 21 so you win!"
    elif cpu_score > user_score and cpu_score < 21:
        return "Opponent is closer to 21 so you lose!"
    elif user_score < cpu_score and user_score < 21:
        return "You win"
    else:
        return "You lose"



def blackjack():
    playing = True

    user_cards = []
    cpu_cards = []

    for i in range(2):
        user_cards.append(deal_card())
        cpu_cards.append(deal_card())

    while playing:

        user_score = score_calculation(user_cards)
        cpu_score = score_calculation(cpu_cards)
        print(f"\n Your cards: {user_cards}, current score: {user_score}")
        print(f" Computer's first card: {cpu_cards[0]}")

        if user_score == 21 or cpu_score == 21 or user_score > 21:
            playing = False
        else:
            deal_another_card = input("Would you like another card? 'Y' or 'N' ").lower()
            if deal_another_card == 'y':
                user_cards.append(deal_card())
            else:
                playing = False

    while cpu_score != 21 and cpu_score < 18:
        cpu_cards.append(deal_card())
        cpu_score = score_calculation(cpu_cards)

    print(f"\n Your final hand: {user_cards}, final score: {user_score}")
    print(f" Computer's final hand: {cpu_cards}, final score: {cpu_score}")
    print(compare_score(user_score, cpu_score))


play = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ").lower()
if play == 'y':
    blackjack()

