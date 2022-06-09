##~~~~~~~~~~~~~~~~-~~~~~~~~~~~~~~~~~##
#             PongPython             #
##~~~~~~~~~~~~~~~~-~~~~~~~~~~~~~~~~~##
######################################
##~~~~~~~~~~~~~~~~-~~~~~~~~~~~~~~~~~##
#              IMPORT                #
##~~~~~~~~~~~~~~~~-~~~~~~~~~~~~~~~~~##
import logging, turtle, random, math
import devconsole

#Logging config
logging.basicConfig(filename="log.txt", filemode="w", level=logging.DEBUG)

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
trace_ray = turtle.Turtle()

ball_list = []
paddle_list = []
ball_color_list = ["purple","yellow","green","pink","gray","brown","blue","lightblue"]
log = []

adding_ia = False
#adding_cheat_mode = False
shock = False

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
    initialisation_screen()
    initialisation_pen()
    initialisation_lp()
    initialisation_rp()
except NameError as ne:
    logging.warning("=================================================================")
    logging.warning(ne.args)
    logging.warning("***Shitty call for initialisation()***")
    logging.warning("***Bad definition for paddle variables***")
    logging.warning("=================================================================")
except AttributeError as ae:
    logging.warning("=================================================================")
    logging.warning(ae.args)
    logging.warning("***Don't touch turtle in initialisation!***")
    logging.warning("=================================================================")


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

"""def activate_cheat():
    global adding_cheat_mode
    adding_cheat_mode = True
    return adding_cheat_mode"""

def playing_with_human():
    screen.onkeypress(leftPaddle_moving_down, "s")
    screen.onkeypress(leftPaddle_moving_up, "z")
    global adding_ia
    adding_ia = False
    return adding_ia

def where_will_it_bounce(ball, direction):
    """
    :param ball: ball where we want to calculate the bouncing
    :param direction:
        BLB, bottom left border
        BRB, bottom right border
        TLB, top left border
        TRB, top right border
    :return: bouncing_point: coordinates of the bouncing
    """
    actual_position = ball.pos()

    if direction == "TLB":
        a_side = ball.distance(ball.xcor(),290) #distance top border
        bouncing_point = (ball.xcor() - a_side, 290)
    elif direction == "TRB":
        a_side = ball.distance(ball.xcor(), 290)
        bouncing_point = (ball.xcor() + a_side, 290)
    elif direction == "BLB":
        a_side = ball.distance(ball.xcor(), -290)
        bouncing_point = (ball.xcor() - a_side, -290) #distance bottom border
    elif direction == "BLB":
        a_side = ball.distance(ball.xcor(), -290)
        bouncing_point = (ball.xcor() + a_side, -290)
    else:
        logging.warning("Not a valid input")
    return bouncing_point


def tracing_cheat_mode(ball, dx, dy):

    global trace_ray
    trace_ray.color("red")
    trace_ray.ht() #hide_turtle
    trace_ray.penup()

    if (dx < 0 and dy < 0) and ball.distance(-200, -290) < DEFAULT_HEIGHT/2: #going to the bottom left side
        bouncing_point = where_will_it_bounce(ball=ball, direction="BLB")
        if 5 < ball.distance(bouncing_point) < 100:  # if bouncing close
            trace_ray.goto(bouncing_point) #setting beginning of trace
            trace_ray.st() #show_turtle
            trace_ray.pendown()
            trace_ray.setheading(135) #setting up angle
            trace_ray.forward(100) #trace until goal
            trace_ray.ht()
            trace_ray.penup()
            return trace_ray



    elif dx > 0 and dy < 0: #going to the bottom right side
        pass
    elif dx < 0 and dy > 0: #going to the top left side
        pass
    else: #going to the top right side
        pass

trace_ray.clear()

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
    ball.speed(3)
    #ball.dx = random.choice([0.2, -0.2, 0.3, -0.3, 0.4, -0.4])
    #ball.dy = random.choice([0.2, -0.2, 0.3, -0.3, 0.4, -0.4])
    ball.dx = -1
    ball.dy = -1
    return ball

### DEVCONSOLE INPUT GETTER AND TREATMENT
def console_take_input():
    arg = screen.textinput("CONSOLE", "")
    value = devconsole.console_input(arg)
    log = devconsole.get_log() # DOESN'T WORK
    if value == 2:
        ball_create()
    

##~~~~~~~~~~~~~~~~-~~~~~~~~~~~~~~~~~##
#         BALL INTERACTION           #
##~~~~~~~~~~~~~~~~-~~~~~~~~~~~~~~~~~##

# BALL MOVEMENT
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
        trace_ray.clear()

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
    #screen.onkeypress(activate_cheat, "c")
    screen.onkeypress(console_take_input, "Tab")
except NameError as ne:
    logging.warning("=================================================================")
    logging.warning(ne.args)
    logging.warning("***Bad definition for paddle variables***")
    logging.warning("=================================================================")

##~~~~~~~~~~~~~~~~-~~~~~~~~~~~~~~~~~##
#               MAIN                 #
##~~~~~~~~~~~~~~~~-~~~~~~~~~~~~~~~~~##


while True:
    for i in ball_list:
        collision_detection(ball=i)
        tracing_cheat_mode(ball=i, dx=i.dx, dy=i.dy)
        if adding_ia:
            adding_bot(ball=i)
        #if adding_cheat_mode:
            #i.pendown()
            #i.pen(speed=60, pencolor="red")
    screen.update()

