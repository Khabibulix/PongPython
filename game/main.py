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
import Paddle
import Ball
import Playground

Playground.screen.listen()
while True:
    Ball.collision_detection()
    Playground.screen.update()

