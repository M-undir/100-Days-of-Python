from turtle import Turtle
TURTLE_POSITIONS = [(-230, -50), (-230, -20), (-230, 10), (-230, 40), (-230, 70), (-230, 100)]
COLORS = ["purple", "orange", "black", "grey", "red", "blue"]


class Race:

    def __init__(self):
        self.colours = COLORS
        self.turtles = []
        self.create_turtle()

    def create_turtle(self):
        for position in range(len(self.colours)):
            new_turtle = Turtle(shape='turtle')
            new_turtle.color(self.colours[position])
            new_turtle.penup()
            new_turtle.goto(TURTLE_POSITIONS[position])
            self.turtles.append(new_turtle)