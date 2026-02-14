from turtle import Turtle
class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.penup()
        self.xm = 12
        self.ym = 12

    def increase_speed(self):
        if self.xm > 0:
            self.xm += 0.5
        else:
            self.xm -= 0.5

        if self.ym > 0:
            self.ym += 0.5
        else:
            self.ym -= 0.5

    def move(self):
        nx = self.xcor()+self.xm
        ny = self.ycor()+self.ym
        self.goto(nx, ny)

    def bounce(self):
        self.ym = -self.ym
    def pbounce(self):
        self.xm = -self.xm