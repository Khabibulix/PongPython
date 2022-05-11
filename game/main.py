# Import and Setup

# "Macro" define
linux = 'linux'
windows = 'win32'


# Import and Setup
## Cross-Plateform Support
"""import sys
import os
if sys.platform.startswith(windows):
    import winsound

def ppgame_playsound(sound):
    if sys.platform.startswith(windows):
        winsound.PlaySound(sound, winsound.SND_ASYNC)
    if sys.platform.startswith(linux):
        os.system("paplay " + sound)"""

import turtle
import winsound
import Ball
import Playground
import Paddle
from Playground import screen, pen, initialisation_pen, initialisation_screen


try:
    initialisation_pen()
except AttributeError as ae:
    print("=================================================================")
    print(ae)
    print("***Problem is in Playground file***")
    print("***or in naming into initialisation_pen***")
    print("=================================================================")

try:
    initialisation_screen()
except AttributeError as ae:
    print("=================================================================")
    print(ae)
    print("***Problem is in Playground file***")
    print("***or in naming into screen***")
    print("=================================================================")

try:
    Ball.initialisation()
except NameError as ne:
    print("=================================================================")
    print(ne)
    print("***Warning in Ball file***")
    print("=================================================================")
except AttributeError as ae:
    print("=================================================================")
    print(ae)
    print("***Don't touch turtle in initialisation!***")
    print("=================================================================")

try:
    Paddle.paddles_initialisation()
except NameError as ne:
    print("=================================================================")
    print(ne)
    print("***Shitty call for initialisation()***")
    print("***Bad definition for paddle variables***")
    print("=================================================================")
except AttributeError as ae:
    print("=================================================================")
    print(ae)
    print("***Don't touch turtle in initialisation!***")
    print("=================================================================")

try:
    Paddle.key_binding()
except NameError as ne:
    print("=================================================================")
    print(ne)
    print("***Bad definition for paddle variables***")
    print("=================================================================")

while True:
    Ball.collision_detection()
    turtle.update()

