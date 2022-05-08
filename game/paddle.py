import turtle
import Playground


class Paddle:
    def __init__(self, xcor):
        self.xcor = xcor

    def initialisation(self, p):
        p = turtle.Turtle()
        p.speed = 0
        p.shape = "square"
        p.color = "white"
        p.shapesize(stretch_wid=5, stretch_len=1)
        p.penup()
        p.goto(self.xcor, 0)

    def moving_up(self, key_pressed):
        screen = Playground.screen
        screen = turtle.Screen()
        if screen.onkeypress(key_pressed):
            y = Paddle.ycor()
            y += 20
            Paddle.sety(y)

    def moving_down(self, key_pressed):
        screen = Playground.screen
        screen = turtle.Screen()
        if screen.onkeypress(key_pressed):
            y = Paddle.ycor()
            y -= 20
            Paddle.sety(y)


left_paddle = Paddle(xcor=-350)
right_paddle = Paddle(xcor=350)

try:
    left_paddle.initialisation(left_paddle)
    left_paddle.initialisation(right_paddle)
except NameError as ne:
    print(ne)
    print("L'appel à initialisation est foireux!")
    print("Ou alors les variables paddle sont mal définies")
except AttributeError as ae:
    print(ae)
    print("Modification du turtle dans initialisation()")


try:
    left_paddle.moving_down(key_pressed="s")
    left_paddle.moving_up(key_pressed="z")
    right_paddle.moving_down(key_pressed="Down")
    right_paddle.moving_up(key_pressed="Up")
except NameError as ne:
    print(ne)
    print("Les variables paddle sont mal définies")
