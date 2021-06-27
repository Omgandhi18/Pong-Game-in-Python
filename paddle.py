from turtle import Turtle
class Paddle(Turtle):

    def __init__(self,position):
        super().__init__()

        self.goto(position)
        self.penup()

        self.shapesize(stretch_wid=5, stretch_len=1)
        self.color("white")
        self.shape("square")