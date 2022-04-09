class ElementMobile:
    def __init__(self, position, speed, shape):
        self.position = position
        self.speed = speed
        self.shape = shape


class Paddle(ElementMobile):
    super().__init__()
    #collision detection avec paddle, méthode paddle
    #mouvement paddle en méthode


class Ball(ElementMobile):
    super.__init__()
    #la balle bouge en méthode

class Pen(ElementMobile):
    super.__init__()
    #le pen dessine le score en méthode
