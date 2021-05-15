from turtle import Turtle, Screen
import time
screen = Screen()
screen.setup(height=600, width=800)
screen.bgcolor('black')
screen.title('Pong')
screen.tracer(0)

# width = 20, height = 100, x_pos = 350, y_pos = 0
paddle = Turtle(shape='square')
paddle.setx(350)
paddle.penup()
paddle.setheading(90)
paddle.shapesize(stretch_wid=1, stretch_len=5)
paddle.color('white')


# Moving the paddle
def up():
    # new_y = paddle.ycor() + 20
    # paddle.sety(new_y)
    paddle.fd(20)


def down():
    paddle.bk(20)


screen.listen()
screen.onkey(key="Up", fun=up)
screen.onkey(key="Down", fun=down)



test_update = True
while test_update:
    screen.update()


screen.exitonclick()
