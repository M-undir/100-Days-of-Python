from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Courier", 15, "normal")  # looks better than Times New Roman


class ScoreBoard(Turtle):

    def __init__(self):
        super().__init__()
        self.color("White")
        self.penup()
        self.ht()
        self.goto(0, 270)
        self.score = 0
        self.update_score()

    def update_score(self):
        self.write(f"Score: {self.score} ", align=ALIGNMENT, font=FONT)

    def add(self):
        self.score += 1
        self.clear()
        self.update_score()

    def game_over(self):  # wall_collision too specific (will die if hit itself too)
        self.goto(-50, 0)
        self.write("Game Over", font=("Times New Roman", 20, "normal"))


