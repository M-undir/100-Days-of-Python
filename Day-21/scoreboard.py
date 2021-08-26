from turtle import Turtle
FONT = ("Courier", 20, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.penup()
        self.hideturtle()
        self.color("Purple")
        self.goto(0, 265)
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(arg=f"Score: {self.score}", font=FONT, align="center")

    def add_score(self):
        self.score += 1
        self.update_scoreboard()

    def game_over(self):
        self.color("White")
        self.goto(0, 0)
        self.write(arg="Game Over", font=FONT, align="center")
