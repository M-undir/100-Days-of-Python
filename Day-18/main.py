import random
import turtle
from colours import colour_list
from turtle import Turtle, Screen
turtle.colormode(255)

hirst_painting = Turtle()
# x and y-axis reach up to 10
# dots are 20 in size and spaced by 50m (.fd(50))

hirst_painting.ht()  # hides the turtle
# hirst_painting.pensize(20)
hirst_painting.penup()
columns_to_complete = 10
y_cor = -200
hirst_painting.goto(x=-200, y=y_cor)

while columns_to_complete > 0:
    for rows in range(10):
        hirst_painting.dot(20, random.choice(colour_list))
        hirst_painting.fd(50)
    y_cor += 50
    hirst_painting.goto(x=-200, y=y_cor)
    columns_to_complete -= 1


screen = Screen()
screen.exitonclick()
