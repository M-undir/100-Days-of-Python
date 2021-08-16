import random
from art import logo


def deal_card():
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    card = random.choice(cards)
    return card


def score_calculator(cards):
    if sum(cards) == 21 and len(cards) == 2:
        return 21
    if 11 in cards[2:]:
        cards.remove(11)
        cards.append(1)
    return sum(cards)


def compare_score(user_score, cpu_score):
    if user_score == 21:
        return "You win by Blackjack"
    elif cpu_score == 21:
        return "CPU wins by Blackjack, you lose!"
    elif cpu_score < user_score < 21:
        return "You are closer to Blackjack, you win!"
    elif 21 < user_score < cpu_score:
        return "You are closer to Blackjack, you win!"
    elif user_score < 21 and cpu_score > 21:
        return "CPU went over, you win!"
    else:
        return "CPU wins"


def blackjack():

    playing = True

    user_cards = []
    cpu_cards = []

    for i in range(2):
        user_cards.append(deal_card())
        cpu_cards.append(deal_card())

    print(logo)

    while playing:
        user_score = score_calculator(user_cards)
        cpu_score = score_calculator(cpu_cards)
        print(f"    Your cards:{user_cards}, current score: {user_score}")
        print(f"    CPU's first card: {cpu_cards[0]}")
        # print(f"{cpu_cards}, score: {cpu_score}")

        if user_score == 21 or user_score > 21 or cpu_score == 21:
            playing = False
        else:
            deal_another_card = input("Type 'y' to get another card, type 'n' to pass: ").lower()
            if deal_another_card == 'y':
                user_cards.append(deal_card())
                # print(user_cards)
            else:
                playing = False

    while cpu_cards != 21 and cpu_score < 18:
        cpu_cards.append(deal_card())
        cpu_score = score_calculator(cpu_cards)

    print(f"    Your final hand: {user_cards}, final score: {user_score}")
    print(f"    Computer's final hand: {cpu_cards}, final score: {cpu_score}")
    print(compare_score(user_score, cpu_score))


while input("Would you like to play a game of Blackjack? Type 'y' or 'n': ") == 'y':
    blackjack()
