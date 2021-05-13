from turtle import Turtle
STARTING_POS = [0, -20, -40]
MOVING_DISTANCE = 20


class Snake:

    def __init__(self):
        self.snake_list = []
        self.create_snake()

    def create_snake(self):
        for pos in STARTING_POS:
            snake_body = Turtle(shape="square")
            snake_body.penup()
            snake_body.color('white')
            snake_body.setx(pos)
            self.snake_list.append(snake_body)

    def move(self):
        # self.create_snake()
        for snake_num in range(len(self.snake_list) - 1, 0, -1):
            prev_x = self.snake_list[snake_num - 1].xcor()
            prev_y = self.snake_list[snake_num - 1].ycor()
            self.snake_list[snake_num].goto(prev_x, prev_y)
        self.snake_list[0].fd(MOVING_DISTANCE)
        # self.snake_list[0].left(90)


# --PREVIOUS CODE-- #

# def snake_movement(self):
#     for snake_num in range(len(self.snake_list)-1, 0, -1):
#         prev_x = self.snake_list[snake_num-1].xcor()
#         prev_y = self.snake_list[snake_num-1].ycor()
#         self.snake_list[snake_num].goto(prev_x, prev_y)
#     self.snake_list[0].fd(20)
    # pass

# for snake_num in range(len(snakes)-1, 0, -1):
#     # previous_co = snakes[snake_num-1].position()
#     previous_x = snakes[snake_num-1].xcor()
#     previous_y = snakes[snake_num-1].ycor()
#     snakes[snake_num].goto(previous_x, previous_y)


# starting_pos = [0, -20, -40]
# snakes = []
#
# for position in starting_pos:
#     snake_body = Turtle(shape='square')
#     snake_body.penup()
#     snake_body.color('white')
#     snake_body.setx(position)
#     snakes.append(snake_body)
#
