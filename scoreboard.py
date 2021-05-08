from turtle import Turtle


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color('white')
        self.penup()
        self.hideturtle()
        self.speed('fastest')

    def create_scoreboard(self, score):
        """Refreshes the scoreboard"""
        self.clear()
        self.goto(0, 0)
        self.write(f"Your Score is {score}", align='center', font=('Courier', 30, 'normal'))


class Level(Turtle):
    def __init__(self):
        super().__init__()
        self.color('white')
        self.penup()
        self.hideturtle()
        self.speed('fastest')

    def create_scoreboard(self, level):
        """Refreshes the scoreboard"""
        self.clear()
        self.goto(290, -200)
        self.write(f"Level: {level}", align='center', font=('Courier', '30', 'normal'))