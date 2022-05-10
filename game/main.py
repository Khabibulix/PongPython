# Import and Setup

# "Macro" define
linux = 'linux'
windows = 'win32'


# Import and Setup
## Cross-Plateform Support
import sys
import os
if sys.platform.startswith(windows):
    import winsound

def ppgame_playsound(sound):
    if sys.platform.startswith(windows):
        winsound.PlaySound(sound, winsound.SND_ASYNC)
    if sys.platform.startswith(linux):
        os.system("paplay " + sound)

import turtle
import winsound
import Playground
import Ball
#import Paddle

try:
    pen = Playground.Pen()
    pen.initialisation(pen)
except AttributeError as ae:
    print(ae)
    print("Le problème est dans le fichier Playground, et dans la dénomination de la classe Pen")

try:
    screen = Playground.Screen()
    screen.initialisation(screen)
except AttributeError as ae:
    print(ae)
    print("***Le problème est dans le fichier Playground, et dans la dénomination de la classe Screen***")

try:
    ball = turtle.Turtle()
    Ball.initialisation(ball)
except NameError as ne:
    print(ne)
    print("***Vérifier nommage de la classe Ball***")
except AttributeError as ae:
    print(ae)
    print("***Modification du turtle dans initialisation() incorrect***")


while True:
    Ball.moving_the_ball()
    turtle.update()

