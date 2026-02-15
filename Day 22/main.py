from turtle import Turtle,Screen
from paddle import Paddle
from ball import Ball
import time
from scoreboard import ScoreBoard

screen = Screen()
screen.setup(width=800, height=600)
screen.title("The Pong Game")
screen.bgcolor("Black")
screen.tracer(0)

l_paddle = Paddle((-360,0))
r_paddle = Paddle((350,0))
ball = Ball()
scoreboard = ScoreBoard()

screen.listen()
screen.onkey(r_paddle.move_up,"Up")
screen.onkey(r_paddle.move_down,"Down")

screen.onkey(l_paddle.move_up,"w")
screen.onkey(l_paddle.move_down,"s")
# WHILE PASSING FUNCTION AS A PARAMETER, NEVER WRITE () <-- THIS.
game_is_on = True
while game_is_on:

    time.sleep(0.1)
    screen.update()
    ball.move()
    # Detect the collision with wall
    if ball.ycor() > 280 or ball.ycor()< -280:
        ball.bounce_y()

    # Detect collision with paddle
    if (ball.distance(r_paddle) < 50 and ball.xcor() > 320) or (ball.distance(l_paddle) < 50 and ball.xcor() < -330):
        ball.bounce_x()

    # Detect when R paddle misses
    if ball.xcor() > 380:
        ball.reset_pos()
        scoreboard.l_point()
    # Detect when L paddle misses
    if ball.xcor() < -380:
        ball.reset_pos()
        scoreboard.r_point()
    

screen.exitonclick()