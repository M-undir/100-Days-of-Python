from turtle import Screen
from snake import Snake
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor('black')
screen.title("Snake")
screen.getshapes()
screen.tracer(0)

snake = Snake()

is_game_on = True

while is_game_on:
    screen.update()
    time.sleep(0.1)

    snake.move()

screen.exitonclick()
