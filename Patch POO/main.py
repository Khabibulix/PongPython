# "Macro" define
linux = 'linux'
windows = 'win32'


# Import and Setup
## Cross-Plateform Support
import sys
if sys.platform.startswith(windows):
    import winsound
## Game
import turtle
import Playground
import Ball
import Paddle

while True:
    turtle.update()
    Ball.collision_detection()
