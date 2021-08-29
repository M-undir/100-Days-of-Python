from turtle import Turtle


class Ball(Turtle):
    def __init__(self):
        super().__init__(shape='circle')
        self.penup()
        self.color('white')
        self.x_move = 10
        self.y_move = 10

    def move(self):
        x = self.xcor() + self.x_move
        # print(x)
        y = self.ycor() + self.y_move
        # print(y)
        # print(x, y)
        self.goto(x, y)

    def bounce(self):
        self.y_move *= -1
        # print(self.y_move)

    def bounce_2(self):
        self.x_move *= -1

    def reset_position(self):
        self.goto(0, 0)
