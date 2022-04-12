import turtle

class ElementMobile:
    def __init__(self, positionX, positionY, speed, shape):
        self.positionX = positionX
        self.positionY = positionY
        self.speed = speed
        self.shape = shape

    def turtle_init(self, element):
        element = turtle.Turtle()

    def where_am_i(self, element):
        element = ElementMobile
        element.goto(self.positionX, self.positionY)


class Paddle(ElementMobile):

    #collision detection avec paddle, méthode paddle
    #mouvement paddle en méthode

    def create_paddle(self, element):
        element.speed = self.speed
        element.shape = self.shape
        element.color = "white"
        element.shapesize(stretch_wid=5, stretch_len=1)
        element.penup()
        element.where_am_i()

"""
class Ball(ElementMobile):
    #la balle bouge en méthode

    def moving_the_ball(self, balle):
        balle.color("white")
        balle.penup()
        balle.where_am_i()
        balle.dx = 0.25
        balle.dy = 0.25"""

"""class Pen(ElementMobile):
    super.__init__(self)
    #le pen dessine le score en méthode
"""


left_paddle = Paddle(0 ,-350,0,"square")
left_paddle.turtle_init(left_paddle)
left_paddle.create_paddle(left_paddle)

right_paddle = Paddle(0,350,0,"square")
right_paddle.turtle_init(right_paddle)
right_paddle.create_paddle(right_paddle)

"""
ball = Ball(positionX=0, positionY=0, speed=0, shpae="turtle")
ball.turtle_init(ball)
ball.moving_the_ball(ball)"""