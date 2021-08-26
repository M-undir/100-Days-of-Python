from turtle import Turtle
NORTH = 90
EAST = 0
SOUTH = 270
WEST = 180
X_POS = [(0, 0), (-20, 0), (-40, 0)]


class Snake:
    def __init__(self):
        self.snake_body = []
        # for i in range(3):
        #     self.create_snake()
        self.create_snake()
        self.snake_head = self.snake_body[0]

    def create_snake(self):
        for position in X_POS:
            self.add_part(position)

    def add_part(self, position):
        snake_segment = Turtle(shape="square")
        snake_segment.penup()
        snake_segment.color("white")
        snake_segment.goto(position)
        self.snake_body.append(snake_segment)

    def extend(self):
        # Add another part to the snake after catching apple
        self.add_part(self.snake_body[-1].position())

    def forward(self):
        if self.snake_head.heading() != SOUTH:
            self.snake_head.setheading(NORTH)

    def backwards(self):
        if self.snake_head.heading() != NORTH:
            self.snake_head.setheading(SOUTH)

    def right(self):
        if self.snake_head.heading() != WEST:
            self.snake_head.setheading(EAST)

    def left(self):
        if self.snake_head.heading() != EAST:
            self.snake_head.setheading(WEST)

    # def create_multiple_segments(self):
    #     for _ in range(2):
    #         self.create_snake_segment()

    def move(self):
        for movement in range(len(self.snake_body) - 1, 0, -1):
            prev_position = self.snake_body[movement-1].position()
            self.snake_body[movement].goto(prev_position)

        self.snake_head.fd(20)
        # self.snake_head.left(90)


# for part in snake_body:
#     part.fd(20)
# snake_head.fd(10)
# snake_head.left(90)
#    # screen.update()
#    # time.sleep(1)

# snake_head.left(90)
# for movement in range(len(snake_body) - 1, 0, -1):
#     # snake_head.fd(20)
#     prev_position = snake_body[movement-1].position()
#     snake_body[movement].goto(prev_position)
#     # snake_head.fd(20)
#     # snake_head.left(90)
#
# # Essentially want the other segments to follow the first segment of the snake body.
# snake_body[0].fd(20)
# # snake_head.right(90)

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
