##~~~~~~~~~~~~~~~~-~~~~~~~~~~~~~~~~~##
#   PongPython - TKinter
##~~~~~~~~~~~~~~~~-~~~~~~~~~~~~~~~~~##
# IMPORT
#
import logging, random, math
import devconsole
import tkinter as tk

##~~~~~~~~~~~~~~~~-~~~~~~~~~~~~~~~~~##
# PINBOARD
#
"""
create_rectangle(x,y,x2,y2)
    (x,y) is the defaults coodinates before tracing
    (x2,y2) is the defaults coodinates after tracing
"""

##~~~~~~~~~~~~~~~~-~~~~~~~~~~~~~~~~~##
# LOGGING CONFIG
#
logging.basicConfig(filename="log.txt", filemode="w", level=logging.DEBUG)

##~~~~~~~~~~~~~~~~-~~~~~~~~~~~~~~~~~##
# MACROS / CONSTANT
#
DEFAULT_WIDTH = 800
DEFAULT_HEIGHT = 600

PRIMARY_COLOR = "black"
SECONDARY_COLOR = "white"

### GAME PARAMETER

BALL_STARTING_ANGLE = 90
BALL_STARTING_SPEED = 0.01

### BALL STRUCTURE (because we don't use class)
BALL_CANVAS = 0     # Contains the TKinter canvas object
BALL_VEC = 1        # Contains a sublist of 2D vector
##
BALL_VECX = 0
BALL_VECY = 1
##
BALL_ANGLE = 2
BALL_SPEED = 3

##~~~~~~~~~~~~~~~~-~~~~~~~~~~~~~~~~~##
# GLOBAL
#
right_paddle_x = 780 # To improve
left_paddle_x = 10 # To improve
paddle_y = DEFAULT_HEIGHT/2  # Quiet efficient, needs a rename

paddle_length = 200 # Has to be deprecated soon

DY = 10 # Has to be deprecated soon
DX = 10 # Has to be deprecated soon

### GAME STATE
score_a = 0
score_b = 0

game_timescale = 1.0

### OBJECTS
paddle_width = DEFAULT_WIDTH / 80
paddle_height = DEFAULT_HEIGHT / 6

ball_width = (DEFAULT_WIDTH + DEFAULT_HEIGHT) / 140

### LISTS (contains the game objects)
list_paddle = []
list_ball = []
list_player = []

##~~~~~~~~~~~~~~~~-~~~~~~~~~~~~~~~~~##
# TK INIT
#
### GAME WINDOW
windows = tk.Tk()
windows.title('Pong Game On Steroids')
windows.geometry(str(DEFAULT_WIDTH)+"x"+str(DEFAULT_HEIGHT))
windows.configure(bg=PRIMARY_COLOR)
windows.resizable(False,False)

### SCORE
scoring = tk.Label(
    windows,
    text=f"Player A: {score_a}\t\tPlayer B: {score_b}",
    foreground=SECONDARY_COLOR,
    background=PRIMARY_COLOR,
    font="consolas"
    )
scoring.pack(ipady=10)

### CANVAS
playground = tk.Canvas(windows,
    width=DEFAULT_WIDTH,
    height=DEFAULT_HEIGHT,
    bg=PRIMARY_COLOR
    )
playground.pack()

##~~~~~~~~~~~~~~~~-~~~~~~~~~~~~~~~~~##
# FUNCTIONS
#
### CONSTRUCTOR
"""TODO"""
left_paddle = playground.create_rectangle(
    left_paddle_x,
    DEFAULT_HEIGHT/2,
    left_paddle_x + 10,
    paddle_length,
    fill=SECONDARY_COLOR)
right_paddle = playground.create_rectangle(
    right_paddle_x,
    DEFAULT_HEIGHT/2,
    right_paddle_x - 10,
    paddle_length,
    fill=SECONDARY_COLOR)

def make_paddle(posX, posY, width, height):
    paddle = playground.create_rectangle(
        posX,           # X1
        posY,           # Y1
        posX + width,   # X2
        posY + height,  # Y2
        fill=SECONDARY_COLOR)
    return paddle

def make_ball(posX, posY, width, angle=BALL_STARTING_ANGLE, speed=BALL_STARTING_SPEED):
    ball = playground.create_oval(
        posX,           # X1
        posY,           # Y1
        posX + width,   # X2
        posY + width,   # Y2
        fill=SECONDARY_COLOR)
    vecX = 0
    vecY = 0
    return [ball,[vecX,vecY],angle,speed]

### GETTER AND SETTER
##### BALL DATA
def ball_get_canvas(ball_id): return list_ball[ball_id][0]
def ball_get_coords(ball_id): return playground.coords(list_ball[ball_id][BALL_CANVAS])
def ball_get_posx(ball_id): return ball_get_coords(ball_id)[0]
def ball_get_posy(ball_id): return ball_get_coords(ball_id)[1]
def ball_get_width(ball_id): return ball_get_coords(ball_id)[2]
def ball_get_height(ball_id): return ball_get_coords(ball_id)[3]
def ball_get_bbox(ball_id): return playground.bbox(list_ball[ball_id][BALL_CANVAS])
def ball_get_vec(ball_id): return list_ball[ball_id][BALL_VEC]
def ball_get_vecx(ball_id): return list_ball[ball_id][BALL_VEC][BALL_VECX]
def ball_get_vecy(ball_id): return list_ball[ball_id][BALL_VEC][BALL_VECY]
def ball_get_angle(ball_id): return list_ball[ball_id][BALL_ANGLE]
def ball_get_speed(ball_id): return list_ball[ball_id][BALL_SPEED]
#
def ball_set_canvas(ball_id, value): list_ball[ball_id][0] = value
def ball_set_posx(ball_id, value): ball_get_coords(ball_id)[0] = value
def ball_set_posy(ball_id, value): ball_get_coords(ball_id)[1] = value
def ball_set_width(ball_id, value): ball_get_coords(ball_id)[2] = value
def ball_set_height(ball_id, value): ball_get_coords(ball_id)[3] = value
def ball_set_vec(ball_id, value): list_ball[ball_id][BALL_VEC] = value
def ball_set_vecx(ball_id, value): list_ball[ball_id][BALL_VEC][BALL_VECX] = value
def ball_set_vecy(ball_id, value): list_ball[ball_id][BALL_VEC][BALL_VECY] = value
def ball_set_angle(ball_id, value): list_ball[ball_id][BALL_ANGLE] = value
def ball_set_speed(ball_id, value): list_ball[ball_id][BALL_SPEED] = value

### PHYSICS
def is_colliding(bbox1, bbox2):
    return (
    bbox1[0] < bbox2[0] + bbox2[2]
    and
    bbox1[0] + bbox1[2] > bbox2[0]
    and
    bbox1[1] < bbox2[1] + bbox2[3]
    and
    bbox1[1] + bbox1[3] > bbox2[1]
    )

def angle_to_vec(angle,speed):
    """Angle is between 0 and 359 (degrees)"""
    vecX = math.cos(math.radians(angle-90))
    vecY = math.sin(math.radians(angle-90))
    vecX *= speed
    vecY *= speed
    return [vecX, vecY]

##### BALL PHYSIC

def ball_update(ball_id):
    """To call when an event change the state of the ball (for exemple a collision)"""
    angle = ball_get_angle(ball_id)
    speed = ball_get_speed(ball_id)
    ball_set_vec(ball_id, angle_to_vec(angle, speed))
    return

def ball_physics(ball_id):
    """Core logic of a ball""" 
    playground.move(ball_get_canvas(ball_id), ball_get_vecx(ball_id), ball_get_vecy(ball_id))
    return

### PRINT AND DEBUG
def print_ball(ball_id):
    print("BALL ", ball_id ," Coords : ", ball_get_coords(ball_id))
    print("BALL ", ball_id ," Bbox : ", ball_get_bbox(ball_id))
    print("BALL ", ball_id ," Vec X = ", ball_get_vecx(ball_id))
    print("BALL ", ball_id ," Vec Y = ", ball_get_vecy(ball_id))
    print("BALL ", ball_id ," Angle = ", ball_get_angle(ball_id))
    print("BALL ", ball_id ," Speed = ", ball_get_speed(ball_id))

### HIGH-LEVEL / USERSIDE FUNCTION
def game_add_ball(posX, posY, width): return list_ball.append(make_ball(posX, posY, width)) # TODO : rename in devconsole

##### I DON'T WHAT IT IS / EXPERIMENT
def for_every(list_object, function):
    """Takes a compatible list, applies a function to each element of it"""
    for i in range(len(list_object)):
        function(i)
    
##~~~~~~~~~~~~~~~~-~~~~~~~~~~~~~~~~~##
# KEY BINDING
#
windows.bind("<Up>", lambda event: playground.move(right_paddle, 0, -5))
windows.bind("<Down>", lambda event: playground.move(right_paddle, 0, 5))
windows.bind("<z>", lambda event: playground.move(left_paddle, 0, -5))
windows.bind("<s>", lambda event: playground.move(left_paddle, 0, 5))
windows.bind("<Escape>", lambda event: windows.destroy())

##~~~~~~~~~~~~~~~~-~~~~~~~~~~~~~~~~~##
# MAIN
#
##### TESTS

list_paddle.append(make_paddle(0, 0, paddle_width, paddle_height)) # Add a new paddle to the game
print(playground.coords(list_paddle[0]))
print(playground.bbox(list_paddle[0]))

### MAIN LOOP

def game_init():
    # OBJECT SPAWN
    game_add_ball(DEFAULT_WIDTH/2, DEFAULT_HEIGHT/2, ball_width)
    # UPDATE
    for_every(list_ball, ball_update)
    # READY
    return

def game_loop():
    for_every(list_ball, ball_physics)
    windows.after(1, game_loop)
    return

game_init()
game_loop()
windows.mainloop()
