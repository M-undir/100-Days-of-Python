from turtle import Screen
from paddle import Paddle
from ball import Ball
import time

screen = Screen()
screen.setup(height=600, width=800)
screen.bgcolor('black')
screen.title('Pong')
screen.tracer(0)

right_paddle = Paddle((350, 0))
left_paddle = Paddle((-350, 0))
ball = Ball()

screen.listen()
screen.onkey(key="Up", fun=right_paddle.up)
screen.onkey(key="Down", fun=right_paddle.down)
screen.onkey(key="s", fun=left_paddle.down)
screen.onkey(key="w", fun=left_paddle.up)


game_on = True
while game_on:
    time.sleep(0.1)
    screen.update()
    ball.move()

screen.exitonclick()
