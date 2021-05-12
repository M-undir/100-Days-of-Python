from turtle import Turtle, Screen

mun = Turtle()
screen = Screen()


def forward():
    mun.fd(10)


def turn_right():
    mun.right(10)


def turn_left():
    mun.left(10)


def backward():
    mun.bk(10)


def clear_drawing():
    mun.reset()


def undo():
    mun.undo()


screen.listen()
screen.onkey(fun=forward, key="Up")
screen.onkey(fun=turn_right, key="Right")
screen.onkey(fun=turn_left, key="Left")
screen.onkey(fun=backward, key="Down")
screen.onkey(fun=clear_drawing, key="z")
screen.onkey(fun=undo, key="u")

screen.exitonclick()
