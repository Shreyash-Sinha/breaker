from turtle import *
from player import Player
from ball import Ball
import time
from blocks import Blocks
from scoreboard import Scoreboard, Level

screen = Screen()
screen.setup(800, 600)
screen.bgcolor('black')
screen.title('Breakout')
screen.tracer(0)

player = Player()
screen.listen()
screen.onkey(player.moveLeft, 'Left')
screen.onkey(player.moveRight, 'Right')
ball = Ball()
gameover = False
lives = 3
neg = False
x = -360
y = 280
blocks = []
score = 0
level = 1
scoreboard = Scoreboard()
run = True
level_ = Level()
level_.create_scoreboard(level)


def generate_mesh():
    global x, y
    for i in range(60):
        block = Blocks((x, y))
        blocks.append(block)
        if x > 350:
            y -= 50
            x = -360
        else:
            x += 65


generate_mesh()
while run:
    if not gameover:
        time.sleep(0.1 * 0.9)
        ball.move()
        screen.update()

        if ball.ycor() > 280:
            ball.bounce_y()

        if ball.xcor() < -380 or ball.xcor() > 380:
            ball.bounce_x()
            neg = True

        if ball.ycor() < -280:
            lives -= 1
            ball.init()

        if ball.xcor() > player.xcor() - 50 and ball.xcor() < player.xcor() + 50 and ball.ycor() < -230:
            ball.bounce_y()

        for i in blocks:
            if i.xcor() > ball.xcor() - 30 and i.xcor() < ball.xcor() + 30 and ball.ycor() < i.ycor() + 15 and ball.ycor() > i.ycor() - 15 and i.isvisible():
                i.hideturtle()
                blocks.remove(i)
                score += 10

        if len(blocks) == 0:
            level += 1
            generate_mesh()
            level_.create_scoreboard(level)
            ball.xm += 1
            ball.ym = 1

        if not lives > 0:
            gameover = True

    if gameover:
        scoreboard.create_scoreboard(score)

screen.exitonclick()