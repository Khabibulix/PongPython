"""linux = 'linux'
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
        os.system("paplay " + sound)"""
import turtle

score_a = 0
score_b = 0
pen = turtle.Turtle()
screen = turtle.Screen()
rightPaddle = turtle.Turtle()
leftPaddle = turtle.Turtle()
ball = turtle.Turtle()


def initialisation_pen():
    pen.speed(0)
    pen.color("white")
    pen.penup()
    pen.hideturtle()
    pen.goto(0, 260)
    pen.write(""
              "Player A: 0\t"
              "Player B: 0",
              align="center",
              font=("Courier", 24, "normal")
              )


def initialisation_screen():
    screen.title("Pong Me If You Can")
    screen.bgcolor("black")
    screen.setup(width=800, height=600)
    screen.tracer(0)
    return screen

try:
    initialisation_screen()
except AttributeError as ae:
    print("=================================================================")
    print(ae)
    print("***Problem is in Playground file***")
    print("***or in naming into screen***")
    print("=================================================================")

try:
    initialisation_pen()
except AttributeError as ae:
    print("=================================================================")
    print(ae)
    print("***Problem is in Playground file***")
    print("***or in naming into initialisation_pen***")
    print("=================================================================")


def initialisation_lp():
    leftPaddle.speed(0)
    leftPaddle.shape("square")
    leftPaddle.color("white")
    leftPaddle.shapesize(stretch_wid=5, stretch_len=1)
    leftPaddle.penup()
    leftPaddle.goto(-350, 0)

def initialisation_rp():
    rightPaddle.speed(0)
    rightPaddle.shape("square")
    rightPaddle.color("white")
    rightPaddle.shapesize(stretch_wid=5, stretch_len=1)
    rightPaddle.penup()
    rightPaddle.goto(350, 0)

try:
    initialisation_lp()
    initialisation_rp()
except NameError as ne:
    print("=================================================================")
    print(ne.args)
    print("***Shitty call for initialisation()***")
    print("***Bad definition for paddle variables***")
    print("=================================================================")
except AttributeError as ae:
    print("=================================================================")
    print(ae.args)
    print("***Don't touch turtle in initialisation!***")
    print("=================================================================")


def leftPaddle_moving_up():
    y = leftPaddle.ycor()
    y += 20
    leftPaddle.sety(y)
def rightPaddle_moving_up():
    y = rightPaddle.ycor()
    y += 20
    rightPaddle.sety(y)
def leftPaddle_moving_down():
    y = leftPaddle.ycor()
    y -= 20
    leftPaddle.sety(y)
def rightPaddle_moving_down():
    y = rightPaddle.ycor()
    y -= 20
    rightPaddle.sety(y)


try:
    screen.listen()
    screen.onkeypress(leftPaddle_moving_down, "s")
    screen.onkeypress(leftPaddle_moving_up, "z")
    screen.onkeypress(rightPaddle_moving_down, "Down")
    screen.onkeypress(rightPaddle_moving_up, "Up")
except NameError as ne:
    print("=================================================================")
    print(ne.args)
    print("***Bad definition for paddle variables***")
    print("=================================================================")


def initialisation():
    ball.shapesize(0.7, 0.7)
    ball.penup()
    ball.goto(0, 0)
    ball.color("white")
    ball.shape("circle")
    ball.speed(0)
    ball.dx = 0.2
    ball.dy = 0.2
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
    global score_a
    global score_b
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
        pen.clear()
        pen.write("Player A: {} \t"
                  "Player B: {}".format(score_a + 1, score_b),
                  align="center",
                  font=("Courier", 24, "normal")
                  )
        score_a += 1

    if ball.xcor() < -390:
        ball.goto(0, 0)
        ball.dx *= -1
        pen.clear()
        pen.write("Player A: {} \t"
                  "Player B: {}".format(score_a, score_b + 1),
                  align="center",
                  font=("Courier", 24, "normal")
                  )
        score_b += 1

    if ball.xcor() > 340 and ball.xcor() < 350 and ball.ycor() < rightPaddle.ycor() + 40 and ball.ycor() > rightPaddle.ycor() - 40:
        ball.setx(340)
        ball.dx *= -1
        #ppgame_playsound("../pong.wav")

    if  ball.xcor() < -340 and ball.xcor() > -350 and ball.ycor() > leftPaddle.ycor() - 40 and ball.ycor() < leftPaddle.ycor() + 40:
        ball.setx(-340)
        ball.dx *= -1
        #ppgame_playsound("../pong.wav")


while True:
    collision_detection()
    screen.update()

