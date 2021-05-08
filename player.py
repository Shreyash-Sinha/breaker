from turtle import *


class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.shape('square')
        self.color('white')
        self.shapesize(stretch_len=7, stretch_wid=1)
        self.penup()
        self.goto((0, -250))
        self.score = 0

    def moveRight(self):
        self.goto((self.xcor()+20, self.ycor()))

    def moveLeft(self):
        self.goto((self.xcor()-20, self.ycor()))