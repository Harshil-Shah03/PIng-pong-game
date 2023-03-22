from turtle import Turtle


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.color('white')
        self.shape('circle')
        self.pu()
        self.x_move = 10
        self.y_move = 10
        self.spd = 0.1
        self.speed(self.spd)

    def move(self):
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)

    def wall_bounce(self):
        self.y_move *= -1

    def paddle_bounce(self):
        self.x_move *= -1
        self.spd *= 0.9

    def reset_pos(self):
        self.goto(0, 0)
        self.x_move *= -1
        self.move()

    def increase_speed(self):
        if self.spd < 10:
            self.spd += 1
            print(self.spd)
        self.speed(self.spd)


