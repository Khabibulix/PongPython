import turtle
import Playground

right_paddle = turtle.Turtle()
left_paddle = turtle.Turtle()
screen = Playground.screen

def initialisation_lp():
    left_paddle.speed(0)
    left_paddle.shape("square")
    left_paddle.color("white")
    left_paddle.shapesize(stretch_wid=5, stretch_len=1)
    left_paddle.penup()
    left_paddle.goto(-350, 0)

def initialisation_rp():
    right_paddle.speed(0)
    right_paddle.shape("square")
    right_paddle.color("white")
    right_paddle.shapesize(stretch_wid=5, stretch_len=1)
    right_paddle.penup()
    right_paddle.goto(350, 0)

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

"""Ici que ça foire, l'appli ne crashe pas mais aucune touche n'est détectée...
Solutions possibles testées:
.Mettre le keybinding dans une fonction et l'appeller depuis main, résultat > import en boucle foireux sans les touches
.J'ai relu la doc turtle, apparemment la syntaxe est bonne
.Tenté avec une lambda depuis stack overflow ici --> Google 'onkeypress function in turtle module problem'
.J'ai débuggué comme j'ai pu, pas de résultats en vue
.Simplification du problème avec la première fonction ci-dessous"""

def left_paddle_moving_up():
    left_paddle.forward(20)
    """y = left_paddle.ycor()
    y += 20
    left_paddle.sety(y)"""
def right_paddle_moving_up():
    """y = right_paddle.ycor()
    y += 20
    left_paddle.sety(y)"""
def left_paddle_moving_down():
    """y = left_paddle.ycor()
    y -= 20
    left_paddle.sety(y)"""
def right_paddle_moving_down():
    """y = right_paddle.ycor()
    y -= 20
    right_paddle.sety(y)"""


try:
    screen.listen()
    screen.onkeypress(left_paddle_moving_down(), "s")
    screen.onkeypress(left_paddle_moving_up(), "z")
    screen.onkeypress(right_paddle_moving_down(), "Down")
    screen.onkeypress(right_paddle_moving_up(), "Up")
except NameError as ne:
    print("=================================================================")
    print(ne.args)
    print("***Bad definition for paddle variables***")
    print("=================================================================")
