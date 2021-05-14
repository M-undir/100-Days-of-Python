from turtle import Turtle
X_POSITIONS = [0, -20, -40]
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake:

    def __init__(self):
        self.snake_list = []
        self.create_snake()
        self.head = self.snake_list[0]

    def create_snake(self):
        for position in X_POSITIONS:
            self.increase_part(position)

    def increase_part(self, position):
        snake_body = Turtle(shape='square')
        snake_body.penup()
        snake_body.color('white')
        snake_body.goto(position, 0)
        self.snake_list.append(snake_body)

    def extend(self):
        # add part to the snake
        self.increase_part(self.snake_list[-1].xcor())

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)




    def move(self):
        for snake_num in range(len(self.snake_list) - 1, 0, -1):
            prev_x = self.snake_list[snake_num - 1].xcor()
            prev_y = self.snake_list[snake_num - 1].ycor()
            self.snake_list[snake_num].goto(prev_x, prev_y)
        self.head.fd(20)

