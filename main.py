from turtle import Screen, Turtle
from paddle import Paddle
from ball import Ball
import time
from scoreboard import ScoreBoard

sb = ScoreBoard()
screen = Screen()
screen.tracer(0)
screen.setup(800, 600)
screen.bgcolor("black")

writer = Turtle()
writer.penup()
writer.goto(x=0, y=300)
writer.pencolor("white")
writer.setheading(270)
while writer.ycor() > -300:
    writer.forward(20)
    writer.pendown()
    writer.forward(20)
    writer.penup()

screen.listen()

ball = Ball()
p1 = Paddle((-360, 0))
p2 = Paddle((360, 0))

screen.onkeypress(fun=p1.go_up, key="w")
screen.onkeypress(fun=p1.go_down, key="s")
screen.onkeypress(fun=p2.go_up, key="Up")
screen.onkeypress(fun=p2.go_down, key="Down")

is_on = True
while is_on:
    time.sleep(0.05)
    screen.update()
    ball.move()

    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce()
    if ((ball.distance(p2) < 51 and ball.xcor() >= 340) or
            (ball.distance(p1) < 51 and ball.xcor() <= -340)):
        ball.pbounce()

    if ball.xcor() > 380:
        ball.goto(0, 0)
        ball.increase_speed()
        sb.increase_right()
        sb.update()

    if ball.xcor() < -380:
        ball.goto(0, 0)
        ball.increase_speed()
        sb.increase_left()
        sb.update()

    if sb.left_point == 10:
        is_on = False
        writer.clear()
        writer.goto(-30, 0)
        sb.clear()
        writer.write("Right Side Won", align="center", font=("Courier", 40))

    if sb.right_point == 10:
        is_on = False
        writer.clear()
        writer.goto(-30, 0)
        sb.clear()
        writer.write("Left Side Won", align="center", font=("Courier", 40))

screen.exitonclick()