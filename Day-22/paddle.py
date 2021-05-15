from turtle import Turtle
# RIGHT_POSITION = (350, 0)
# LEFT_POSITION = (-350, 0)
STRETCH_WIDTH = 1
STRETCH_HEIGHT = 5
HEADING = 90
FORWARD_MOVEMENT = 20


class Paddle(Turtle):
    
    def __init__(self, position):
        super().__init__()
        self.shape('square')
        self.goto(position)
        self.penup()
        self.setheading(HEADING)
        self.shapesize(stretch_wid=STRETCH_WIDTH, stretch_len=STRETCH_HEIGHT)
        self.color('white')

    def up(self):
        self.fd(FORWARD_MOVEMENT)

    def down(self):
        self.bk(FORWARD_MOVEMENT)
