from turtle import Turtle, Screen
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor('black')
screen.title("Snake")
screen.getshapes()
screen.tracer(0)


starting_pos = [0, -20, -40]
snakes = []

for position in starting_pos:
    snake_body = Turtle(shape='square')
    snake_body.penup()
    snake_body.color('white')
    snake_body.setx(position)
    snakes.append(snake_body)

screen.update()

is_game_on = True
while is_game_on:
    screen.update()
    time.sleep(0.1)
    # for body in snakes:
    #     body.fd(10)
    # snakes[0].fd(10)
    # snakes[1].goto(snakes[0].position)
    # snakes[2].goto(snakes[1].position)
    for snake_num in range(len(snakes)-1, 0, -1):
        # previous_co = snakes[snake_num-1].position()
        previous_x = snakes[snake_num-1].xcor()
        previous_y = snakes[snake_num-1].ycor()
        snakes[snake_num].goto(previous_x, previous_y)
    snakes[0].fd(20)
    snakes[0].left(90)
screen.exitonclick()
