from turtle import Screen
from paddle import Paddle
from ball import Ball
from score import Score
import time

screen = Screen()
screen.setup(height=600, width=800)
screen.bgcolor('black')
screen.title('Pong')
screen.tracer(0)

right_paddle = Paddle((350, 0))
left_paddle = Paddle((-350, 0))
ball = Ball()
score = Score()

screen.listen()
screen.onkeypress(key="Up", fun=right_paddle.up)
screen.onkeypress(key="Down", fun=right_paddle.down)
screen.onkeypress(key="s", fun=left_paddle.down)
screen.onkeypress(key="w", fun=left_paddle.up)


game_on = True
while game_on:
    time.sleep(ball.ball_speed)
    screen.update()
    ball.move()

    if ball.ycor() > 280 or ball.ycor() < -280:
        # needs to be propelled backwards/forwards (bounce)
        ball.y_bounce()

    # Detect collision w right paddle

    if ball.distance(right_paddle) < 50 and ball.xcor() > 330 or ball.distance(left_paddle) < 50 and ball.xcor() < -330:
        # print("Contact")
        ball.x_bounce()

    # Right paddle miss
    if ball.xcor() > 390:
        # print("Out of bounds")
        ball.reset_pos()
        score.add_l_score()
    # Left paddle miss
    if ball.xcor() < -390:
        ball.reset_pos()
        score.add_r_score()
screen.exitonclick()
