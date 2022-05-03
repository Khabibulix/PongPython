import turtle
import Playground


class Paddle:
    def __init__(self, speed, shape, color, xcor):
        self.speed = speed
        self.shape = shape
        self.color = color
        self.xcor = xcor

    def initialisation(self, p):
        p.shapesize(stretch_wid=5, stretch_len=1)
        p.penup()
        p.goto(paddle.xcor, 0)

    def moving_up(self, key_pressed):
        screen = Playground.creating_playground()
        if screen.onkeypress(key_pressed):
            y = Paddle.ycor()
            y += 20
            Paddle.sety(y)


    def moving_down(self, key_pressed):
        screen = Playground.creating_playground()
        if screen.onkeypress(key_pressed):
            y = Paddle.ycor()
            y -= 20
            Paddle.sety(y)


left_paddle = Paddle(speed=0, shape="square", color="white", xcor=-350)
right_paddle = Paddle(speed=0, shape="square", color="white", xcor=350)
left_paddle = turtle.Turtle()
right_paddle = turtle.Turtle()
Paddle.initialisation(left_paddle)
Paddle.initialisation(right_paddle)
left_paddle.moving_down(key_pressed="s")
left_paddle.moving_up(key_pressed="z")
right_paddle.moving_down(key_pressed="Down")
right_paddle.moving_up(key_pressed="Up")