from turtle import Turtle
FONT = ("Courier", 20, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.ht()
        self.penup()
        self.right_score = 0
        self.left_score = 0
        self.winner = None
        self.color('white')
        self.goto(-50, 200)
        self.write(f"{self.left_score}  {self.right_score}", font=("Arial", 50, "normal"))

    def update_scoreboard(self):
        self.clear()
        self.write(f"{self.left_score}  {self.right_score}", font=("Arial", 50, "normal"))

    def game_over(self):
        if self.right_score > self.left_score:
            self.winner = 'right'
        else:
            self.winner = 'left'
        self.goto(-140, 0)
        self.color('white')
        self.write(f"The {self.winner} side wins.", font=("Courier", 20, "normal"))
