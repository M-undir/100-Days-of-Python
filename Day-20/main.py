from turtle import Screen
from snake import Snake
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake")
screen.listen()
screen.tracer(0)

snake = Snake()
screen.onkey(fun=snake.forward, key ="Up")
screen.onkey(fun=snake.backwards, key ="Down")
screen.onkey(fun=snake.right, key ="Right")
screen.onkey(fun=snake.left, key ="Left")


game = True
while game:
    screen.update()
    time.sleep(0.1)

    snake.move()


screen.exitonclick()
