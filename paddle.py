from turtle import Turtle
class Paddle(Turtle):

    def __init__(self,position):
        super().__init__()
        self.shape("square")
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.goto(position)
        self.color("white")
        self.penup()

    def go_up(self):
        if self.ycor() < 250:
            newy = self.ycor()+20
            self.goto(x=self.xcor(), y=newy)

    def go_down(self):
        if self.ycor() > -240:
            newy = self.ycor()-20
            self.goto(x=self.xcor(), y=newy)
