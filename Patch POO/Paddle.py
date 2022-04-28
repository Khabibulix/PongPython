import turtle

class Paddle():
    def __init__(self, speed=int, shape=str, color=str, xcor=int):
        speed = self.speed
        shape = self.shape
        color = self.color
        xcor = self.xcor

    def moving_up(self, key_pressed):
        if screen.onkeypress(key_pressed):
            y = Paddle.ycor()
            y += 20
            Paddle.sety(y)


    def moving_down(self, key_pressed):
        if screen.onkeypress(key_pressed):
            y = Paddle.ycor()
            y -= 20
            Paddle.sety(y)

    def initialisation(self, paddle):
        Paddle = turtle.Turtle()
        Paddle.shapesize(stretch_wid=5, stretch_len=1)
        Paddle.penup()
        Paddle.goto(paddle.xcor, 0)


def creating_paddles():
    left_paddle = Paddle(speed=0, shape="square", color="white", xcor=-350)
    right_paddle = Paddle(speed=0, shape="square", color="white", xcor=350)
    Paddle.initialisation(left_paddle)
    Paddle.initialisation(right_paddle)
    left_paddle.moving_down(key_pressed="s")
    left_paddle.moving_up(key_pressed="z")
    right_paddle.moving_down(key_pressed="Down")
    right_paddle.moving_up(key_pressed="Up")