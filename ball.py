from turtle import Turtle


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape('circle')
        self.color('white')
        self.penup()
        self.shapesize(stretch_len=1, stretch_wid=1)
        self.goto((0, 0))
        self.ym = 10
        self.xm = 10
        self.velocity = 1.0

    def move(self):
        x = self.xcor() + self.xm
        y = self.ycor() + self.ym
        self.goto((x, y))

    def bounce_y(self):
        self.ym *= -1

    def bounce_x(self):
        self.xm *= -1

    def init(self):
        self.goto((0, 0))
        self.ym = 10
        self.xm = 10
        self.velocity = 0.1
