from turtle import Turtle, Screen
import turtle
import random

screen = Screen()
screen.setup(width=500, height=400)
winner_guess = turtle.textinput("Turtle Race", "Who will win?:").lower()
is_racing = False
colours = ["purple", "orange", "black", "grey", "red", "blue"]
turtles = []


y = -50

for i in range(len(colours)):
    new_turtle = Turtle(shape='turtle')
    new_turtle.color(colours[i])
    new_turtle.penup()
    new_turtle.goto(-230, y)
    y += 30
    # new_turtle.forward(random.randint(1, 10))
    turtles.append(new_turtle)


if winner_guess:
    is_racing = True

while is_racing:

    for chosen_turtle in turtles:
        if chosen_turtle.xcor() > 230:
            is_racing = False
            winner = chosen_turtle.pencolor()
            if winner == winner_guess:
                print("You guess it right!")
            else:
                print(f"The winner was the {winner} turtle.")

        random_pace = random.randint(0, 10)
        chosen_turtle.fd(random_pace)


screen.exitonclick()
