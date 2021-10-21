from turtle import Screen
from line import Line
from paddle import Paddle
from ball import Ball
from scoreboard import ScoreBoard
import time

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.tracer(0)
screen.title("Pong Game")
line = Line()

r_paddle = Paddle(350, 0)
l_paddle = Paddle(-350, 0)
ball = Ball()
scoreboard = ScoreBoard()

screen.listen()
screen.onkey(r_paddle.up, "Up")
screen.onkey(r_paddle.down, "Down")
screen.onkey(l_paddle.up, "w")
screen.onkey(l_paddle.down, "s")


game_is_on = True

while game_is_on:
    screen.update()
    time.sleep(ball.move_speed)
    ball.move()

    if ball.ycor() > 275 or ball.ycor() < -275:
        ball.bounce_y()

    if ball.xcor() > 410:
        scoreboard.add_left_score()
        ball.reset_position()
        r_paddle.paddle_reset()
        l_paddle.paddle_reset()

    if ball.xcor() < -410:
        scoreboard.add_right_score()
        ball.reset_position()
        r_paddle.paddle_reset()
        l_paddle.paddle_reset()

    if ball.distance(r_paddle) < 45 and ball.xcor() == 340 or ball.distance(l_paddle) < 45 and ball.xcor() == -340:
        ball.bounce_x()

    if scoreboard.left_score == 5 or scoreboard.right_score == 5:
        game_is_on = False

        if scoreboard.left_score == 5:
            scoreboard.game_over_left()

        else:
            scoreboard.game_over_right()

screen.exitonclick()
