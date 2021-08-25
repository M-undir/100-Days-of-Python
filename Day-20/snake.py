from turtle import Turtle
NORTH = 90
EAST = 0
SOUTH = 270
WEST = 180


class Snake:
    def __init__(self):
        self.x_pos = [0, -20, -40]
        self.snake_body = []
        self.create_snake()

    def create_snake(self):
        for body in self.x_pos:
            snake_segment = Turtle(shape="square")
            snake_segment.penup()
            snake_segment.color("white")
            snake_segment.setx(body)
            self.snake_body.append(snake_segment)

    def forward(self):
        if self.snake_body[0].heading() != SOUTH:
            self.snake_body[0].setheading(NORTH)

    def backwards(self):
        if self.snake_body[0].heading() != NORTH:
            self.snake_body[0].setheading(SOUTH)

    def right(self):
        if self.snake_body[0].heading() != WEST:
            self.snake_body[0].setheading(EAST)

    def left(self):
        if self.snake_body[0].heading() != EAST:
            self.snake_body[0].setheading(WEST)

    # def create_multiple_segments(self):
    #     for _ in range(2):
    #         self.create_snake_segment()

    def move(self):
        for movement in range(len(self.snake_body) - 1, 0, -1):
            prev_position = self.snake_body[movement-1].position()
            self.snake_body[movement].goto(prev_position)

        self.snake_body[0].fd(20)
        # self.snake_body[0].left(90)



# for part in snake_body:
#     part.fd(20)
# snake_body[0].fd(10)
# snake_body[0].left(90)
#    # screen.update()
#    # time.sleep(1)

# snake_body[0].left(90)
# for movement in range(len(snake_body) - 1, 0, -1):
#     # snake_body[0].fd(20)
#     prev_position = snake_body[movement-1].position()
#     snake_body[movement].goto(prev_position)
#     # snake_body[0].fd(20)
#     # snake_body[0].left(90)
#
# # Essentially want the other segments to follow the first segment of the snake body.
# snake_body[0].fd(20)
# # snake_body[0].right(90)

# 3 squares, looks like they'll be connected to each other.

# x_pos =
#
#
# for body in x_pos:
#     snake_segment = Turtle(shape="square")
#     snake_segment.penup()
#     snake_segment.color("white")
#     snake_segment.setx(body)
#     snake_body.append(snake_segment)