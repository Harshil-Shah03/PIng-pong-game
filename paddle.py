from turtle import Turtle


class Paddle(Turtle):
    def __init__(self, xpos, ypos):
        super().__init__()
        self.pu()
        self.color("white")
        self.shape("square")
        self.seth(90)
        self.shapesize(stretch_wid=1, stretch_len=5)
        self.x = xpos
        self.y = ypos
        self.paddle_setup()

    def paddle_setup(self):
        self.pu()
        self.speed("fastest")
        self.goto(self.x, self.y)

    def paddle_up(self):
        self.fd(20)

    def paddle_down(self):
        self.bk(20)
