from turtle import Turtle
class ScoreBoard(Turtle):

    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.pencolor("white")
        self.left_point = 0
        self.right_point = 0
        self.goto(x=50,y=250)
        self.write(str(self.left_point), align="center", font=("Courier", 30))
        self.goto(x=-50, y=250)
        self.write(str(self.right_point), align="center", font=("Courier", 30))

    def increase_right(self):
        self.right_point += 1
    def increase_left(self):
        self.left_point += 1

    def update(self):
        self.clear()
        self.penup()
        self.goto(x=50,y=250)
        self.write(str(self.left_point), align="center", font=("Courier", 30))
        self.goto(x=-50, y=250)
        self.write(str(self.right_point), align="center", font=("Courier", 30))