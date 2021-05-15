from turtle import Turtle
START_POSITION = (350, 0)
STRETCH_WIDTH = 1
STRETCH_HEIGHT = 5
HEADING = 90
FORWARD_MOVEMENT = 20


class Paddle:
    
    def __init__(self):
        self.paddle = Turtle()
        self.create_paddle()
    
    def create_paddle(self):
        self.paddle = Turtle(shape='square')
        self.paddle.goto(START_POSITION)
        self.paddle.penup()
        self.paddle.setheading(HEADING)
        self.paddle.shapesize(stretch_wid=STRETCH_WIDTH, stretch_len=STRETCH_HEIGHT)
        self.paddle.color('white')

    def up(self):
        self.paddle.fd(FORWARD_MOVEMENT)

    def down(self):
        self.paddle.bk(FORWARD_MOVEMENT)


# Issue: Method 'create_self.paddle' may be 'static'
