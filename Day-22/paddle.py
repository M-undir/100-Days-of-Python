from turtle import Turtle
COLOR = 'white'


class Paddle(Turtle):
    def __init__(self, position):
        super().__init__(shape='square')
        self.penup()
        self.color(COLOR)
        self.shapesize(stretch_wid=4, stretch_len=1)
        self.goto(position)
        self.forward_movement = 25
        self.backward_movement = 25

    # def right_paddle_position(self):
    #     self.goto(375, 0)
    #
    # def left_paddle_position(self):
    #     self.goto(-375, 0)

    def forwards(self):
        y = self.ycor()
        y += self.forward_movement
        return self.sety(y)

    def backwards(self):
        y = self.ycor()
        y -= self.backward_movement
        return self.sety(y)

    def stop_forward(self):
        self.forward_movement = 0

    def stop_backward(self):
        self.backward_movement = 0

    def reset_values(self):
        self.backward_movement = 25
        self.forward_movement = 25
