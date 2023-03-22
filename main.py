from turtle import Screen
from paddle import Paddle
from ball import Ball
from score_board import ScoreBoard
import time

LEFT_XPOS = -350
LEFT_YPOS = 0
RIGHT_XPOS = 350
RIGHT_YPOS = 0
screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.tracer(0)
player_1 = Paddle(LEFT_XPOS, LEFT_YPOS)
player_2 = Paddle(RIGHT_XPOS, RIGHT_YPOS)

ball = Ball()
score_board = ScoreBoard()
screen.listen()

screen.onkey(key="w", fun=player_1.paddle_up)
screen.onkey(key="s", fun=player_1.paddle_down)

screen.onkey(key="Up", fun=player_2.paddle_up)
screen.onkey(key="Down", fun=player_2.paddle_down)
game_is_on = True
while game_is_on:
    time.sleep(ball.spd)
    screen.update()
    ball.move()

    # Detect collision with wall
    if abs(ball.ycor()) > 288:
        ball.wall_bounce()

    # Player 2 misses
    if ball.xcor() >= 360:
        ball.reset_pos()
        score_board.p1_point()
        ball.spd = 0.1
    # Player 1 misses
    if ball.xcor() <= -360:
        ball.reset_pos()
        score_board.p2_point()
        ball.spd = 0.1
    # Detect paddle collision
    if ball.distance(player_2) < 45 and ball.xcor() > 320 or ball.distance(player_1) < 45 and ball.xcor() < -320:
        ball.paddle_bounce()

screen.exitonclick()
