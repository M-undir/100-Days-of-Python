from turtle import Turtle


class Score(Turtle):

    def __init__(self):
        super().__init__()
        self.color('white')
        self.penup()
        self.ht()
        self.left_score = 0
        self.right_score = 0
        self.sety(200)
        self.update_score()

    def update_score(self):
        self.clear()
        self.write(f"{self.left_score}    {self.right_score}", align='center', font=("Courier", 50, "normal"))

    def add_l_score(self):
        self.left_score += 1
        self.update_score()

    def add_r_score(self):
        self.right_score += 1
        self.update_score()


