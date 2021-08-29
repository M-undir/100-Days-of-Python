"""
Steps:
    Create Screen -> Created the Screen (without the scoreboard yet)
    Create and move paddle - Done
    Create another paddle - Done
    Create ball and make it move - Done
    Detect collision with wall and make ball bounce - Done
    Detect collision with paddle - Done
    Detect when paddle misses (add score to opposing side) - Done
    Keep score
"""

from turtle import Screen
from paddle import Paddle
from setup import Setup
from ball import Ball
from scoreboard import Scoreboard
import time

Y_POS = [290, -290]
COLOR = 'white'


screen = Screen()
screen.bgcolor('black')

screen.setup(width=800, height=600)
screen.tracer(0)
screen.listen()

scoreboard = Scoreboard()

setup = Setup(290)
setup2 = Setup(-290)

right_paddle = Paddle((375, 0))
left_paddle = Paddle((-375, 0))

ball = Ball()

screen.onkeypress(fun=left_paddle.forwards, key='w')
screen.onkeypress(fun=left_paddle.backwards, key='s')

screen.onkeypress(fun=right_paddle.forwards, key='Up')
screen.onkeypress(fun=right_paddle.backwards, key='Down')

playing_pong = True

while playing_pong:
    screen.update()
    time.sleep(0.05)
    ball.move()

    # Limit it's movement inside the border
    if right_paddle.ycor() > 220:
        right_paddle.forward_movement = 0
    elif right_paddle.ycor() < -220:
        right_paddle.backward_movement = 0
    else:
        right_paddle.reset_values()

    if left_paddle.ycor() > 220:
        left_paddle.forward_movement = 0
    elif left_paddle.ycor() < -220:
        left_paddle.backward_movement = 0
    else:
        left_paddle.reset_values()

    # Make the ball bounce
    if ball.ycor() > 255 or ball.ycor() < -255:
        ball.bounce()
    if ball.xcor() > 365 and ball.distance(right_paddle) < 50 or ball.xcor() < -365 and ball.distance(left_paddle) < 50:
        ball.bounce_2()

    # Detect if right paddle misses ball
    if ball.xcor() > 390:
        scoreboard.left_score += 1
        ball.reset_position()
        scoreboard.update_scoreboard()

    # Detect if left paddle misses ball
    if ball.xcor() < -390:
        scoreboard.right_score += 1
        ball.reset_position()
        scoreboard.update_scoreboard()

    # End game when it reaches score of 10
    if scoreboard.left_score == 10 or scoreboard.right_score == 10:
        scoreboard.game_over()
        playing_pong = False

    # Why a 50 pixel distance?
    # Since the distance measures the center of the ball from the center of the paddle
    # It doesn't care about the edges of the paddle so the distance is larger than 20 by a lot (50)

screen.exitonclick()
