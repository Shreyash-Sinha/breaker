from turtle import Turtle
import random


class Blocks(Turtle):
    def __init__(self, position):
        super().__init__()
        self.shape('square')
        self.color(random.choice(['red', 'blue', 'green', 'yellow', 'orange']))
        self.shapesize(stretch_len=3, stretch_wid=2)
        self.penup()
        self.goto(position)