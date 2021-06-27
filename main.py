import time
from turtle import Screen
from paddle import Paddle
from ball import Ball
from score import Score
screen=Screen()
screen.setup(width=800,height=600)
screen.bgcolor("black")
screen.title("Pong")
screen.tracer(0)
r_paddle=Paddle((350,0))
l_paddle=Paddle((-350,0))
ball=Ball()
scoreboard=Score()


def rgo_up():
    new_y=r_paddle.ycor()+20
    r_paddle.goto(r_paddle.xcor(),new_y)
def rgo_down():
    new_y=r_paddle.ycor()-20
    r_paddle.goto(r_paddle.xcor(),new_y)
def lgo_up():
    new_y=l_paddle.ycor()+20
    l_paddle.goto(l_paddle.xcor(),new_y)
def lgo_down():
    new_y=l_paddle.ycor()-20
    l_paddle.goto(l_paddle.xcor(),new_y)


screen.listen()

screen.onkey(rgo_up,"Up")
screen.onkey(rgo_down,"Down")
screen.onkey(lgo_up,"w")
screen.onkey(lgo_down,"s")
game_is_on=True
while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()

    ball.move_ball()
    if ball.ycor()>290:
        ball.bounce_y()
    elif ball.ycor()<-290:
        ball.bounce_y()
    if ball.distance(r_paddle)<50 and ball.xcor()>330 or ball.distance(l_paddle)<50 and ball.xcor()<-330:
        ball.bounce_x()
    if ball.xcor()>380:
        ball.reset_position()
        print(ball.move_speed)
        scoreboard.l_point()

    if ball.xcor()<-380:
        ball.reset_position()
        scoreboard.r_point()




screen.exitonclick()