from turtle import Turtle
import random

# x -> between -300 to 300
# y -> between -300 to 300


class Food(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.color("purple")
        self.speed("fastest")  # faster animation, doesn't waste time
        self.new_location()

    def new_location(self):
        random_x = random.randint(-260, 260)
        random_y = random.randint(-260, 260)
        self.goto(random_x, random_y)