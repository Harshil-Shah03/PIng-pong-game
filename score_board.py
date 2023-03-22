from turtle import Turtle


class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.pu()
        self.hideturtle()
        self.p1_score = 0
        self.p2_score = 0
        self.update_b()

    def update_b(self):
        self.goto(-100, 200)
        self.write(self.p1_score, align="center", font=("Courier", 80, "normal"))
        self.goto(100, 200)
        self.write(self.p2_score, align="center", font=("Courier", 80, "normal"))

    def p1_point(self):
        self.clear()
        self.p1_score += 1
        self.update_b()

    def p2_point(self):
        self.clear()
        self.p2_score += 1
        self.update_b()
