from turtle import Turtle
import random


class Food(Turtle):

    def __init__(self):
        super().__init__(shape='circle')
#       self.shape('circle')
        self.penup()
#       Circle is 20x20, we want it to be 10x10
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.color("dark slate blue")
        self.speed("fastest")
        self.new_location()

    def new_location(self):
        random_x = random.randint(-280, 280)
        random_y = random.randint(-280, 280)
        self.goto(random_x, random_y)
