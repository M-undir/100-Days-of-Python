from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake")
screen.listen()
screen.tracer(0)

snake = Snake()

screen.onkey(fun=snake.forward, key="Up")
screen.onkey(fun=snake.backwards, key="Down")
screen.onkey(fun=snake.right, key="Right")
screen.onkey(fun=snake.left, key="Left")

food = Food()
scoreboard = Scoreboard()

game = True
while game:
    screen.update()
    time.sleep(0.1)
    snake.move()

    # Detect collision with wall
    # end_wall = (-280, -0)
    # if snake.snake_head.distance():  # or if snake.snake_head.distance(-280):
    #     print(random.randint(1,100))

    if snake.snake_head.xcor() < -285 or snake.snake_head.ycor() < -285 or snake.snake_head.xcor() > 285 or snake.snake_head.ycor() > 295:
        # print("You've surpassed your limits")
        # print(random.randint(1, 100))
        scoreboard.game_over()
        game = False

    # Detect collision with tail
    for i in snake.snake_body[1:]:
        if snake.snake_head.distance(i) < 15:
            scoreboard.game_over()
            game = False

    # Detect collision with food
    distance = snake.snake_head.distance(food)
    if distance < 20:
        food.new_location()
        scoreboard.add_score()
        snake.extend()


screen.exitonclick()
