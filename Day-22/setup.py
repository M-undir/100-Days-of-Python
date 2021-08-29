from turtle import Turtle


class Setup(Turtle):
    def __init__(self, position):
        super().__init__()
        self.penup()
        self.goto(0, 295)
        self.setheading(270)
        self.color('white')
        self.width(5)
        self.draw_line()
        # self.shape('turtle')
        self.border(position)

    def draw_line(self):
        for _ in range(30):
            self.pendown()
            self.fd(15)
            self.penup()
            self.fd(15)

    def border(self, position):
        self.shape('square')
        self.setheading(90)
        self.shapesize(stretch_wid=100, stretch_len=2)
        self.color('white')
        self.penup()
        self.sety(position)
