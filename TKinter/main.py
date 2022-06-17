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

PADDLE_STARTING_SPEED = 0.1

BALL_STARTING_ANGLE = 45
BALL_STARTING_SPEED = 0.1

### STRUCTURES (because we don't use class)
##### PADDLE STRUCTURE
PADDLE_CANVAS = 0 # Contains the TKinter canvas object
PADDLE_VEC = 1
PADDLE_KEYSET = 2
###
PADDLE_KEYSET_MOVEUP = 0
PADDLE_KEYSET_MOVEDOWN = 1
###
PADDLE_SPEED = 3
PADDLE_STATE = 4
###
PADDLE_STATE_UP = 0
PADDLE_STATE_DOWN = 1

##### BALL STRUCTURE
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
game_score = [0, 0]

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
    text=f"Player A: {game_score[0]}\t\tPlayer B: {game_score[1]}",
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
def make_paddle(posX, posY, width, height, key_moveup="<z>", key_movedown="<s>", speed=PADDLE_STARTING_SPEED, up=False, down=False):
    paddle = playground.create_rectangle(
        posX,           # X1
        posY,           # Y1
        posX + width,   # X2
        posY + height,  # Y2
        fill=SECONDARY_COLOR)
    vecY = 0
    return [paddle, vecY, [key_moveup,key_movedown], speed, [up, down]]

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
##### PADDLE DATA
def paddle_get_canvas(paddle_id): return list_paddle[paddle_id][0]
def paddle_get_coords(paddle_id): return playground.coords(list_paddle[paddle_id][PADDLE_CANVAS])
def paddle_get_posx(paddle_id): return paddle_get_coords(paddle_id)[0]
def paddle_get_posy(paddle_id): return paddle_get_coords(paddle_id)[1]
def paddle_get_width(paddle_id): return paddle_get_coords(paddle_id)[2] - paddle_get_coords(paddle_id)[0]
def paddle_get_height(paddle_id): return paddle_get_coords(paddle_id)[3] - paddle_get_coords(paddle_id)[1]
def paddle_get_bbox(paddle_id): return playground.bbox(list_paddle[paddle_id][PADDLE_CANVAS])
def paddle_get_vec(paddle_id): return list_paddle[paddle_id][PADDLE_VEC]
def paddle_get_key_moveup(paddle_id): return list_paddle[paddle_id][PADDLE_KEYSET][PADDLE_KEYSET_MOVEUP]
def paddle_get_key_movedown(paddle_id): return list_paddle[paddle_id][PADDLE_KEYSET][PADDLE_KEYSET_MOVEDOWN]
def paddle_get_speed(paddle_id): return list_paddle[paddle_id][PADDLE_SPEED]
def paddle_get_state_up(paddle_id): return list_paddle[paddle_id][PADDLE_STATE][PADDLE_STATE_UP]
def paddle_get_state_down(paddle_id): return list_paddle[paddle_id][PADDLE_STATE][PADDLE_STATE_DOWN]
#
def paddle_set_canvas(paddle_id, value): list_paddle[paddle_id][0] = value
def paddle_set_posx(paddle_id, value): paddle_get_coords(paddle_id)[0] = value
def paddle_set_posy(paddle_id, value): paddle_get_coords(paddle_id)[1] = value
# TOFIX def paddle_set_width(paddle_id, value): paddle_get_coords(paddle_id)[2] = value
# TOFIX def paddle_set_height(paddle_id, value): paddle_get_coords(paddle_id)[3] = value
def paddle_set_vec(paddle_id, value): list_paddle[paddle_id][PADDLE_VEC] = value
def paddle_set_key_moveup(paddle_id, value): list_paddle[paddle_id][PADDLE_KEYSET][PADDLE_KEYSET_MOVEUP] = value
def paddle_set_key_movedown(paddle_id, value): list_paddle[paddle_id][PADDLE_KEYSET][PADDLE_KEYSET_MOVEDOWN] = value
def paddle_set_speed(paddle_id, value): list_paddle[paddle_id][PADDLE_SPEED] = value
def paddle_set_state_up(paddle_id, value): list_paddle[paddle_id][PADDLE_STATE][PADDLE_STATE_UP] = value
def paddle_set_state_down(paddle_id, value): list_paddle[paddle_id][PADDLE_STATE][PADDLE_STATE_DOWN] = value
##### BALL DATA
def ball_get_canvas(ball_id): return list_ball[ball_id][0]
def ball_get_coords(ball_id): return playground.coords(list_ball[ball_id][BALL_CANVAS])
def ball_get_posx(ball_id): return ball_get_coords(ball_id)[0]
def ball_get_posy(ball_id): return ball_get_coords(ball_id)[1]
def ball_get_width(ball_id): return ball_get_coords(ball_id)[2] - ball_get_coords(ball_id)[0]
def ball_get_height(ball_id): return ball_get_coords(ball_id)[3] - ball_get_coords(ball_id)[1]
def ball_get_bbox(ball_id): return playground.bbox(list_ball[ball_id][BALL_CANVAS])
def ball_get_vec(ball_id): return list_ball[ball_id][BALL_VEC]
def ball_get_vecx(ball_id): return list_ball[ball_id][BALL_VEC][BALL_VECX]
def ball_get_vecy(ball_id): return list_ball[ball_id][BALL_VEC][BALL_VECY]
def ball_get_angle(ball_id): return list_ball[ball_id][BALL_ANGLE]
def ball_get_speed(ball_id): return list_ball[ball_id][BALL_SPEED]
#
def ball_set_canvas(ball_id, value): list_ball[ball_id][0] = value
# def ball_set_posx(ball_id, value): ball_get_coords(ball_id)[0] = value # DEPRECATED - USE BALL_TELEPORT() INSTEAD
# def ball_set_posy(ball_id, value): ball_get_coords(ball_id)[1] = value # DEPRECATED - USE BALL_TELEPORT() INSTEAD
def ball_set_vec(ball_id, value): list_ball[ball_id][BALL_VEC] = value
def ball_set_vecx(ball_id, value): list_ball[ball_id][BALL_VEC][BALL_VECX] = value
def ball_set_vecy(ball_id, value): list_ball[ball_id][BALL_VEC][BALL_VECY] = value
def ball_set_angle(ball_id, value): list_ball[ball_id][BALL_ANGLE] = value
def ball_set_speed(ball_id, value): list_ball[ball_id][BALL_SPEED] = value
#
def ball_teleport(ball_id, posx, posy):
    begx = ball_get_posx(ball_id)
    begy = ball_get_posy(ball_id)
    dir = lambda a, b : (a - b) * -1
    playground.move(ball_get_canvas(ball_id), dir(begx, posx), dir(begy, posy))
    return
    

### PHYSICS / PROCESS
def is_colliding(ball_id, paddle_id):
    return (
        ball_get_posx(ball_id) < paddle_get_posx(paddle_id) + paddle_get_width(paddle_id)
        and
        paddle_get_posx(paddle_id) < ball_get_posx(ball_id) + ball_get_width(ball_id)
        and
        ball_get_posy(ball_id) < paddle_get_posy(paddle_id) + paddle_get_height(paddle_id)
        and
        paddle_get_posy(paddle_id) < ball_get_posy(ball_id) + ball_get_height(ball_id) 
        )

def angle_to_vec(angle,speed):
    """Angle is between 0 and 359 (degrees)"""
    vecX = math.cos(math.radians(angle-90))
    vecY = math.sin(math.radians(angle-90))
    vecX *= speed
    vecY *= speed
    return [vecX, vecY]

##### PADDLE PHYSIC
def paddle_setup(paddle_id):
    windows.bind(paddle_get_key_moveup(paddle_id), lambda event: paddle_set_state_up(paddle_id, True))
    windows.bind(paddle_get_key_movedown(paddle_id), lambda event: paddle_set_state_down(paddle_id, True))

def paddle_physics(paddle_id):
    if paddle_get_state_up(paddle_id):
        playground.move(paddle_get_canvas(paddle_id), 0, -5)
        paddle_set_state_up(paddle_id, False)
    if paddle_get_state_down(paddle_id):
        playground.move(paddle_get_canvas(paddle_id), 0, 5)
        paddle_set_state_down(paddle_id, False)
    return

##### BALL PHYSIC
def ball_reset(ball_id):
    ball_teleport(ball_id, DEFAULT_WIDTH/2, DEFAULT_HEIGHT/2)
    return
    
def ball_switch_direction(ball_id, angle):
    ball_angle = ball_get_angle(ball_id)
    ball_set_angle(ball_id, ball_angle + angle)
    ball_update(ball_id)
    return

def ball_checkbounds(ball_id):
    posx = ball_get_posx(ball_id)
    posy = ball_get_posy(ball_id)
    width = ball_get_width(ball_id)
    height = ball_get_height(ball_id)
    if posy + height >= DEFAULT_HEIGHT or posy < 0: # TOP / BOTTOM
        ball_switch_direction(ball_id, 90)
    if posx + width >= DEFAULT_WIDTH: # RIGHT
        game_score[0] += 1
        ball_reset(ball_id)
    if posx < 0: # LEFT
        game_score[1] += 1
        ball_reset(ball_id)
    return
        

def ball_update(ball_id):
    """To call when an event change the state of the ball (for exemple a collision)"""
    angle = ball_get_angle(ball_id)
    speed = ball_get_speed(ball_id)
    ball_set_vec(ball_id, angle_to_vec(angle, speed))
    return

def ball_physics(ball_id):
    """Core logic of a ball""" 
    playground.move(ball_get_canvas(ball_id), ball_get_vecx(ball_id), ball_get_vecy(ball_id))
    for paddle_id in range(len(list_paddle)):
        if is_colliding(ball_id, paddle_id):
            print("Collision with ", paddle_id)
            ball_switch_direction(ball_id, 90)
    ball_checkbounds(ball_id)
    return

### PRINT AND DEBUG
def print_paddle(paddle_id):
    print("PADDLE ", paddle_id ," Canvas : ", paddle_get_canvas(paddle_id))
    print("PADDLE ", paddle_id ," Coords : ", paddle_get_coords(paddle_id))
    print("PADDLE ", paddle_id ," Bbox : ", paddle_get_bbox(paddle_id))
    print("PADDLE ", paddle_id ," Width : ", paddle_get_width(paddle_id))
    print("PADDLE ", paddle_id ," Height : ", paddle_get_height(paddle_id))
    print("PADDLE ", paddle_id ," Vec = ", paddle_get_vec(paddle_id))
    print("PADDLE ", paddle_id ," Key MOVEUP = ", paddle_get_key_moveup(paddle_id))
    print("PADDLE ", paddle_id ," Key MOVEDOWN = ", paddle_get_key_movedown(paddle_id))
    print("PADDLE ", paddle_id ," Speed = ", paddle_get_speed(paddle_id))
    print("PADDLE ", paddle_id ," UP = ", paddle_get_state_up(paddle_id))
    print("PADDLE ", paddle_id ," DOWN = ", paddle_get_state_down(paddle_id))

def print_ball(ball_id):
    print("BALL ", ball_id ," Canvas : ", ball_get_canvas(ball_id))
    print("BALL ", ball_id ," Coords : ", ball_get_coords(ball_id))
    print("BALL ", ball_id ," Bbox : ", ball_get_bbox(ball_id))
    print("BALL ", ball_id ," Width : ", ball_get_width(ball_id))
    print("BALL ", ball_id ," Height : ", ball_get_height(ball_id))  
    print("BALL ", ball_id ," Vec X = ", ball_get_vecx(ball_id))
    print("BALL ", ball_id ," Vec Y = ", ball_get_vecy(ball_id))
    print("BALL ", ball_id ," Angle = ", ball_get_angle(ball_id))
    print("BALL ", ball_id ," Speed = ", ball_get_speed(ball_id))

### HIGH-LEVEL / USERSIDE FUNCTION
def game_add_paddle(posX, posY, width, height, key_moveup="<z>", key_movedown="<s>", speed=PADDLE_STARTING_SPEED):
    return list_paddle.append(make_paddle(posX, posY, width, height, key_moveup, key_movedown, speed))
def game_add_ball(posX, posY, width): return list_ball.append(make_ball(posX, posY, width)) # TODO : rename in devconsole

##### I DON'T WHAT IT IS / EXPERIMENT
def for_every(list_object, function):
    """Takes a compatible list, applies a function to each element of it"""
    for i in range(len(list_object)):
        function(i)
    
##~~~~~~~~~~~~~~~~-~~~~~~~~~~~~~~~~~##
# KEY BINDING
#
windows.bind("<Escape>", lambda event: windows.destroy())

##~~~~~~~~~~~~~~~~-~~~~~~~~~~~~~~~~~##
# MAIN
#
def game_init():
    # OBJECT SPAWN
    game_add_paddle(left_paddle_x, DEFAULT_HEIGHT/2, paddle_width, paddle_height, "<z>", "<s>")
    game_add_paddle(right_paddle_x,DEFAULT_HEIGHT/2, paddle_width, paddle_height, "<Up>", "<Down>")
    for_every(list_paddle, paddle_setup)
    game_add_ball(DEFAULT_WIDTH/2, DEFAULT_HEIGHT/2, ball_width)
    # UPDATE
    for_every(list_ball, ball_update)
    # READY
    return

def game_loop():
    for_every(list_paddle, paddle_physics) # Paddles have priority over balls in manner to punish less the players
    for_every(list_ball, ball_physics)
    windows.after(1, game_loop)
    return

game_init()
game_loop()
windows.mainloop()
