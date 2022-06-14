import turtle, random, math, os, sys, winsound

DEFAULT_WIDTH = 800
DEFAULT_HEIGHT = 600
MOVING_DISTANCE = 20
DEFAULT_XPOS_LEFT_GOAL = -350
DEFAULT_XPOS_RIGHT_GOAL = 350
UP_BORDER = 290
DOWN_BORDER = -290

score_a = 0
score_b = 0

pen = turtle.Turtle()
screen = turtle.Screen()
rightPaddle = turtle.Turtle()
leftPaddle = turtle.Turtle()

ball_list = []
color_list = ["purple","yellow","green","pink","gray","brown","blue","lightblue"]

adding_ia = False
shock = False

##~~~~~~~~~~~~~~~~-~~~~~~~~~~~~~~~~~##
#              FUNCTIONS             #
##~~~~~~~~~~~~~~~~-~~~~~~~~~~~~~~~~~##

def ppgame_playsound(sound):
    if sys.platform.startswith("win"):
        winsound.PlaySound(sound, winsound.SND_ASYNC)
    if sys.platform.startswith("lin"):
        os.system("paplay " + sound)

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

def initialisation_lp():
    leftPaddle.speed(0)
    leftPaddle.shape("square")
    leftPaddle.color(random.choice(color_list))
    leftPaddle.shapesize(stretch_wid=5, stretch_len=1)
    leftPaddle.penup()
    leftPaddle.goto(DEFAULT_XPOS_LEFT_GOAL, 0)
    return leftPaddle

def initialisation_rp():
    rightPaddle.speed(0)
    rightPaddle.shape("square")
    rightPaddle.color(random.choice(color_list))
    rightPaddle.shapesize(stretch_wid=5, stretch_len=1)
    rightPaddle.penup()
    rightPaddle.goto(DEFAULT_XPOS_RIGHT_GOAL, 0)
    return rightPaddle

try:
    initialisation_screen()
    initialisation_pen()
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

##~~~~~~~~~~~~~~~~-~~~~~~~~~~~~~~~~~##
#              USER INPUT            #
##~~~~~~~~~~~~~~~~-~~~~~~~~~~~~~~~~~##

def leftPaddle_moving_up():
    y = leftPaddle.ycor()
    y += MOVING_DISTANCE
    leftPaddle.sety(y)

def rightPaddle_moving_up():
    y = rightPaddle.ycor()
    y += MOVING_DISTANCE + 10
    rightPaddle.sety(y)

def leftPaddle_moving_down():
    y = leftPaddle.ycor()
    y -= MOVING_DISTANCE
    leftPaddle.sety(y)

def rightPaddle_moving_down():
    y = rightPaddle.ycor()
    y -= MOVING_DISTANCE + 10
    rightPaddle.sety(y)

def ball_create():
    global ball_list
    ball_list.append(ball_initialisation())

def activate_ia():
    global adding_ia
    adding_ia = True
    return adding_ia

def playing_with_human():
    screen.onkeypress(leftPaddle_moving_down, "s")
    screen.onkeypress(leftPaddle_moving_up, "z")
    global adding_ia
    adding_ia = False
    return adding_ia

##~~~~~~~~~~~~~~~~-~~~~~~~~~~~~~~~~~##
#            BALL INIT               #
##~~~~~~~~~~~~~~~~-~~~~~~~~~~~~~~~~~##

def ball_initialisation():
    ball = turtle.Turtle()
    ball.penup()
    ball.shapesize(0.7, 0.7)
    ball.goto(0, 0)
    ball.color(random.choice(color_list))
    ball.shape("circle")
    ball.speed(1)
    ball.dx = random.choice([0.2, -0.2, 0.3, -0.3, 0.4, -0.4])
    ball.dy = random.choice([0.2, -0.2, 0.3, -0.3, 0.4, -0.4])
    return ball


def collision_detection(ball):
    """
    Adding collision detection to the ball. If it encounters a border or a paddlle, it bounces back
    :param ball:
    :return: None
    """
    global shock
    global score_a
    global score_b
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    #bouncing on top
    if ball.ycor() > UP_BORDER:
        ball.sety(UP_BORDER)
        ball.dy *= -1
        ppgame_playsound("pong.wav")
        ball.clear()

    #bouncing on bottom
    if ball.ycor() < DOWN_BORDER:
        ball.sety(DOWN_BORDER)
        ball.dy *= -1
        ppgame_playsound("pong.wav")
        ball.clear()

    #left goal
    if ball.xcor() > DEFAULT_XPOS_RIGHT_GOAL + 40:
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

    #right goal
    if ball.xcor() < DEFAULT_XPOS_LEFT_GOAL - 40:
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

    #bouncing on right paddle


    bntrb = ball.xcor() > 340 and ball.xcor() < 350 # ball next to right border
    borp = ball.ycor() < rightPaddle.ycor() + 50 and ball.ycor() > rightPaddle.ycor() - 50 #ball on right paddle

    bntlb = ball.xcor() < -340 and ball.xcor() > -350 # ball next to left border
    bolp = ball.ycor() > leftPaddle.ycor() - 50 and ball.ycor() < leftPaddle.ycor() + 50 #ball on left paddle

    #bouncing on right paddle
    if bntrb and borp:
        ball.setx(340)
        ball.dx *= random.choice([-0.8, -0.9, -1])
        ppgame_playsound("pong.wav")
        shock = True
        ball.clear()
    #bouncing on left paddle
    if bntlb and bolp:
        ball.setx(-340)
        ball.dx *= random.choice([-0.8, -0.9, -1])
        ppgame_playsound("pong.wav")
        shock = True
        ball.clear()

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
        collision_detection(ball=i)
        if adding_ia:
            adding_bot(i)
    screen.update()