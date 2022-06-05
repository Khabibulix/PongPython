##~~~~~~~~~~~~~~~~-~~~~~~~~~~~~~~~~~##
#             PongPython             #
##~~~~~~~~~~~~~~~~-~~~~~~~~~~~~~~~~~##
######################################
##~~~~~~~~~~~~~~~~-~~~~~~~~~~~~~~~~~##
#              IMPORT                #
##~~~~~~~~~~~~~~~~-~~~~~~~~~~~~~~~~~##
import turtle
import random
import math
""" SOUND - UNUSED
# Import and Setup
## Cross-Plateform Support
import sys
import os
if sys.platform.startswith(windows):
    import winsound
"""
##~~~~~~~~~~~~~~~~-~~~~~~~~~~~~~~~~~##
#               MACRO                #
##~~~~~~~~~~~~~~~~-~~~~~~~~~~~~~~~~~##
""" SOUND - UNUSED
OS_LINUX = 'linux'
OS_LINUX = 'win32'
"""
DEFAULT_WIDTH = 800
DEFAULT_HEIGHT = 600
##~~~~~~~~~~~~~~~~-~~~~~~~~~~~~~~~~~##
#              GLOBAL                #
##~~~~~~~~~~~~~~~~-~~~~~~~~~~~~~~~~~##
score_a = 0
score_b = 0
pen = turtle.Turtle()
screen = turtle.Screen()
rightPaddle = turtle.Turtle()
leftPaddle = turtle.Turtle()
ball_list = []
paddle_list = []
adding_ia = False
adding_cheat_mode = False
shock = False
ball_color_list = ["purple","yellow","green","pink","gray","brown","blue","lightblue"]

""" SOUND - UNUSED
def ppgame_playsound(sound):
    if sys.platform.startswith(windows):
        winsound.PlaySound(sound, winsound.SND_ASYNC)
    if sys.platform.startswith(linux):
        os.system("paplay " + sound)
"""
##~~~~~~~~~~~~~~~~-~~~~~~~~~~~~~~~~~##
#              FUNCTIONS             #
##~~~~~~~~~~~~~~~~-~~~~~~~~~~~~~~~~~##

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
    screen.setup(width = DEFAULT_WIDTH, height = DEFAULT_HEIGHT)
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
    return leftPaddle

def initialisation_rp():
    rightPaddle.speed(0)
    rightPaddle.shape("square")
    rightPaddle.color("white")
    rightPaddle.shapesize(stretch_wid=5, stretch_len=1)
    rightPaddle.penup()
    rightPaddle.goto(350, 0)
    return rightPaddle

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


def adding_bot(ball):
   global shock
   #if the ball is coming fast from the other side, we moves, else we do nothing
   if ball.xcor() < -100 and ball.ycor():
        if ball.ycor() < leftPaddle.ycor() and not shock:
            leftPaddle.speed(50)
            leftPaddle_moving_down()
        if ball.ycor() > leftPaddle.ycor() and not shock:
            leftPaddle.speed(50)
            leftPaddle_moving_up()
   else:
        shock = False


def activate_ia():
    global adding_ia
    adding_ia = True
    return adding_ia

def activate_cheat():
    global adding_cheat_mode
    adding_cheat_mode = True
    return adding_cheat_mode

def playing_with_human():
    screen.onkeypress(leftPaddle_moving_down, "s")
    screen.onkeypress(leftPaddle_moving_up, "z")
    global adding_ia
    adding_ia = False
    return adding_ia

##~~~~~~~~~~~~~~~~-~~~~~~~~~~~~~~~~~##
#              USER INPUT            #
##~~~~~~~~~~~~~~~~-~~~~~~~~~~~~~~~~~##

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

def ball_create():
    global ball_list
    ball_list.append(ball_initialisation())

def paddle_create():
    global paddle_list
    paddle_list.append(initialisation_lp())
    paddle_list.append(initialisation_rp())


def ball_initialisation():
    ball = turtle.Turtle()
    ball.penup()
    ball.shapesize(0.7, 0.7)
    ball.goto(0, 0)
    ball.color(random.choice(ball_color_list))
    ball.shape("circle")
    ball.speed(40)
    ball.dx = random.choice([0.2, -0.2, 0.3, -0.3, 0.4, -0.4])
    ball.dy = random.choice([0.2, -0.2, 0.3, -0.3, 0.4, -0.4])
    return ball



# BALL MOVEMENT
def collision_detection(ball):
    """
    Adding collision detection to the ball. If it encounters a border or a paddlle, it bounces back
    :param ball:
    :return:
    """
    global shock
    global score_a
    global score_b
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    if ball.ycor() > 290:
    # inverse direction de la balle
        ball.sety(290)
        ball.dy *= -1
        ball.clear()
        #ppgame_playsound("../pong.wav")

    if ball.ycor() < -290:
        ball.sety(-290)
        ball.dy *= -1
        ball.clear()
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
        ball.clear()

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
        ball.clear()

    if ball.xcor() > 340 and ball.xcor() < 350 and ball.ycor() < rightPaddle.ycor() + 40 and ball.ycor() > rightPaddle.ycor() - 40:
        ball.setx(340)
        ball.dx *= -1
        shock = True
        ball.clear()
        #ppgame_playsound("../pong.wav")

    if  ball.xcor() < -340 and ball.xcor() > -350 and ball.ycor() > leftPaddle.ycor() - 40 and ball.ycor() < leftPaddle.ycor() + 40:
        ball.setx(-340)
        ball.dx *= -1
        shock = True
        ball.clear()
        #ppgame_playsound("../pong.wav")

##~~~~~~~~~~~~~~~~-~~~~~~~~~~~~~~~~~##
#               INPUT                #
##~~~~~~~~~~~~~~~~-~~~~~~~~~~~~~~~~~##

try:
    screen.listen()
    screen.onkeypress(playing_with_human, "2")
    screen.onkeypress(activate_ia, "1")
    screen.onkeypress(rightPaddle_moving_down, "Down")
    screen.onkeypress(rightPaddle_moving_up, "Up")
    screen.onkeypress(ball_create, "p")
    screen.onkeypress(activate_cheat, "c")



except NameError as ne: 
    print("=================================================================")
    print(ne.args)
    print("***Bad definition for paddle variables***")
    print("=================================================================")

##~~~~~~~~~~~~~~~~-~~~~~~~~~~~~~~~~~##
#               MAIN                 #
##~~~~~~~~~~~~~~~~-~~~~~~~~~~~~~~~~~##
while True:
    for i in ball_list:
        collision_detection(i)
        if adding_ia:
            adding_bot(i)
        if adding_cheat_mode:
            i.pendown()
            i.pen(speed=60, pencolor="red")
    screen.update()

