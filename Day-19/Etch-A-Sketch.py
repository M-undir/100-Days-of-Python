from turtle import Turtle, Screen

new_turtle = Turtle()
screen = Screen()


def forward():
    new_turtle.fd(10)


def turn_right():
    new_turtle.right(10)


def turn_left():
    new_turtle.left(10)


def backward():
    new_turtle.bk(10)


def clear_drawing():
    new_turtle.reset()


def undo():
    new_turtle.undo()


screen.listen()
screen.onkey(fun=forward, key="Up")
screen.onkey(fun=turn_right, key="Right")
screen.onkey(fun=turn_left, key="Left")
screen.onkey(fun=backward, key="Down")
screen.onkey(fun=clear_drawing, key="z")
screen.onkey(fun=undo, key="u")

screen.exitonclick()
