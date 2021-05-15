from turtle import Screen
from paddle import Paddle

screen = Screen()
screen.setup(height=600, width=800)
screen.bgcolor('black')
screen.title('Pong')
screen.tracer(0)


paddle = Paddle()


screen.listen()
screen.onkey(key="Up", fun=paddle.up)
screen.onkey(key="Down", fun=paddle.down)


test_update = True
while test_update:
    screen.update()


screen.exitonclick()
