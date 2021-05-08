from turtle import Turtle, Screen
import random
is_racing = False
screen = Screen()
screen.setup(width=500, height=400)
screen.title("The Turtle Race")
user_bet = screen.textinput("Make your bet", "Who'll win the race? Enter a colour:").lower()
colors = ["black", "red", "grey", "green", "blue", "purple"]

turtles = []

y = -70
for i in range(6):
    new_turtle = Turtle()
    new_turtle.penup()
    new_turtle.color(colors[i])
    new_turtle.shape("turtle")
    new_turtle.goto(-240, y)
    turtles.append(new_turtle)
    y += 30

if user_bet:
    is_racing = True

while is_racing:

    for turtle in turtles:
        if turtle.xcor() > 230:
            is_racing = False
            color_won = turtle.pencolor()
            if color_won == user_bet:
                print(f"You have guessed the winner!The winner was {color_won}.")
            else:
                print(f"You guessed wrong. The winner was {color_won}")


        random_pace = random.randint(0, 10)
        turtle.forward(random_pace)


screen.exitonclick()

