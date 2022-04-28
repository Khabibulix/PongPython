# Import and Setup
import turtle
import winsound
import Playground
import Ball
import Paddle


# Preparing game
Playground.creating_playground()
Paddle.creating_paddles()
Ball.creating_ball()

#Main game
while True:
    turtle.update()
    Ball.ball.collision_detection()




