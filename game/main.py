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
from Playground import *
from Ball import *
from Paddle import *


while True:
    turtle.update()
    collision_detection(ball)

