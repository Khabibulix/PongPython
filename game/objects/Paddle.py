import turtle
import Playground


right_paddle = turtle.Turtle()
left_paddle = turtle.Turtle()

def initialisation_rp():
    right_paddle.speed = 0.2
    right_paddle.shape = "square"
    right_paddle.color = "white"
    right_paddle.shapesize(stretch_wid=5, stretch_len=1)
    right_paddle.penup()
    right_paddle.goto(350, 0)

def initialisation_lp():
    left_paddle.speed = 0.2
    left_paddle.shape = "square"
    left_paddle.color = "white"
    left_paddle.shapesize(stretch_wid=5, stretch_len=1)
    left_paddle.penup()
    left_paddle.goto(-350, 0)

try:
    initialisation_lp()
    initialisation_rp()
except NameError as ne:
    print("=================================================================")
    print(ne.args)
    print("***Shitty call for initialisation()***")
    print("***Bad definition for paddle variables***")
    print("=================================================================")
except AttributeError as ae:
    print("=================================================================")
    print(ae.args)
    print("***Don't touch turtle in initialisation!***")
    print("=================================================================")


def left_paddle_moving_up(key_pressed):
    if Playground.screen.onkeypress(key_pressed):
        y = left_paddle.ycor()
        y += 20
        left_paddle.sety(y)

def right_paddle_moving_up(key_pressed):
    if Playground.screen.onkeypress(key_pressed):
        y = right_paddle.ycor()
        y += 20
        left_paddle.sety(y)

def left_paddle_moving_down(key_pressed):
    if Playground.screen.onkeypress(key_pressed):
        y = left_paddle.ycor()
        y -= 20
        left_paddle.sety(y)

def right_paddle_moving_down(key_pressed):
    if Playground.screen.onkeypress(key_pressed):
        y = right_paddle.ycor()
        y -= 20
        right_paddle.sety(y)

def key_binding():
    left_paddle_moving_down(key_pressed="s")
    left_paddle_moving_up(key_pressed="z")
    right_paddle_moving_down(key_pressed="Down")
    right_paddle_moving_up(key_pressed="Up")

try:
    key_binding()
except NameError as ne:
    print("=================================================================")
    print(ne.args)
    print("***Bad definition for paddle variables***")
    print("=================================================================")


