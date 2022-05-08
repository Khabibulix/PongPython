import turtle

class Ball:

    def initialisation(self, b):
        b = turtle.Turtle()
        b.shapesize(0.7, 0.7)
        b.penup()
        b.goto(0, 0)
        #vitesse de la balle
        b.dx = 0.25
        b.dy = 0.25
        #direction de la balle
        b.setx(b.xcor() + b.dx)
        b.sety(b.ycor() + b.dy)


try:
    ball = Ball()
    ball.initialisation(ball)
except NameError as ne:
    print(ne)
    print("Vérifier nommage de la classe Ball")
except AttributeError as ae:
    print(ae)
    print("Modification du turtle dans initialisation() incorrect")


def collision_detection(balle):
    if balle.ycor() > 290:
    # inverse direction de la balle
        balle.sety(290)
        balle.dy *= -1
        ppgame_playsound("../pong.wav")

    if balle.ycor() < -290:
        balle.sety(-290)
        balle.dy *= -1
        ppgame_playsound("../pong.wav")

    if balle.xcor() > 390:
        balle.goto(0, 0)
        balle.dx *= -1
        score_a += 1
        pen.clear()
        pen.write("Player A: {} \t"
                  "Player B: {}".format(score_a, score_b),
                  align="center",
                  font=("Courier", 24, "normal")
                  )

    if balle.xcor() < -390:
        balle.goto(0, 0)
        balle.dx *= -1
        score_b += 1
        pen.clear()
        pen.write("Player A: {} \t"
                  "Player B: {}".format(score_a, score_b),
                  align="center",
                  font=("Courier", 24, "normal")
                  )

    if balle.xcor() > 340 and balle.xcor() < 350 and balle.ycor() < rightPaddle.ycor() + 40 and balle.ycor() > rightPaddle.ycor() - 40:
        balle.setx(340)
        balle.dx *= -1
        ppgame_playsound("../pong.wav")

    if  balle.xcor() < -340 and balle.xcor() > -350 and balle.ycor() > leftPaddle.ycor() - 40 and balle.ycor() < leftPaddle.ycor() + 40:
        balle.setx(-340)
        balle.dx *= -1
        ppgame_playsound("../pong.wav")