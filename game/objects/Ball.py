import turtle

def initialisation(balle):
    balle = turtle.Turtle()
    balle.shapesize(0.7, 0.7)
    balle.penup()
    balle.goto(0, 0)
    balle.color("white")
    balle.shape("turtle")


def moving_the_ball():
    ball = turtle.Turtle()
    ball.dx = 0.25
    ball.dy = 0.25
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)
    return ball



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