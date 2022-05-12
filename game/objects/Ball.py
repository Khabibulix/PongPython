import turtle

ball = turtle.Turtle()

def initialisation():
    ball.shapesize(0.7, 0.7)
    ball.penup()
    ball.goto(0, 0)
    ball.color("yellow")
    ball.shape("circle")
    ball.speed(0)
    ball.dx = 0.15
    ball.dy = 0.15
    return ball


try:
    initialisation()
except NameError as ne:
    print("=================================================================")
    print(ne.args)
    print("***Warning in Ball file***")
    print("=================================================================")
except AttributeError as ae:
    print("=================================================================")
    print(ae.args)
    print("***Don't touch turtle in initialisation!***")
    print("=================================================================")


def collision_detection():
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    if ball.ycor() > 290:
    # inverse direction de la balle
        ball.sety(290)
        ball.dy *= -1
        #ppgame_playsound("../pong.wav")

    if ball.ycor() < -290:
        ball.sety(-290)
        ball.dy *= -1
        #ppgame_playsound("../pong.wav")

    if ball.xcor() > 390:
        ball.goto(0, 0)
        ball.dx *= -1
        """score_a += 1
        pen.clear()
        pen.write("Player A: {} \t"
                  "Player B: {}".format(score_a, score_b),
                  align="center",
                  font=("Courier", 24, "normal")
                  )"""

    if ball.xcor() < -390:
        ball.goto(0, 0)
        ball.dx *= -1
        """score_b += 1
        pen.clear()
        pen.write("Player A: {} \t"
                  "Player B: {}".format(score_a, score_b),
                  align="center",
                  font=("Courier", 24, "normal")
                  )"""

    """if ball.xcor() > 340 and ball.xcor() < 350 and ball.ycor() < rightPaddle.ycor() + 40 and ball.ycor() > rightPaddle.ycor() - 40:
        ball.setx(340)
        ball.dx *= -1
        ppgame_playsound("../pong.wav")

    if  ball.xcor() < -340 and ball.xcor() > -350 and ball.ycor() > leftPaddle.ycor() - 40 and ball.ycor() < leftPaddle.ycor() + 40:
        ball.setx(-340)
        ball.dx *= -1
        ppgame_playsound("../pong.wav")"""


