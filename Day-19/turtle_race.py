from turtle import Screen
from race import Race
import turtle
import random

screen = Screen()
screen.setup(width=500, height=400)
winner_guess = turtle.textinput("Turtle Race", "Who will win?:").lower()
is_racing = False


race = Race()

if winner_guess:
    is_racing = True

while is_racing:
    for chosen_turtle in race.turtles:
        if chosen_turtle.xcor() > 230:
            is_racing = False
            winner = chosen_turtle.pencolor()
            if winner == winner_guess:
                print("You guess it right!")
            else:
                print(f"The winner was the {winner} turtle.")
        rand_pace = random.randint(0, 10)
        chosen_turtle.fd(rand_pace)

screen.exitonclick()
