##~~~~~~~~~~~~~~~~-~~~~~~~~~~~~~~~~~##
#   PongPython - TKinter
##~~~~~~~~~~~~~~~~-~~~~~~~~~~~~~~~~~##
# IMPORT
#
import logging, random, math
import devconsole
import tkinter as tk

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

##~~~~~~~~~~~~~~~~-~~~~~~~~~~~~~~~~~##
# GLOBAL
#

ball_x = 375 # Has to be deprecated soon
ball_y = 275 # Has to be deprecated soon

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

### LISTS

list_paddle = []
list_ball = []
list_player = []

##~~~~~~~~~~~~~~~~-~~~~~~~~~~~~~~~~~##
# OBJECTS INIT
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

### PADDLE
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
"""
create_rectangle(x,y,x2,y2)
    (x,y) is the defaults coodinates before tracing
    (x2,y2) is the defaults coodinates after tracing
"""

### BALL
ball = playground.create_oval(
    ball_x,
    ball_y,
    ball_x + 10,
    ball_y + 10,
    fill=SECONDARY_COLOR)

##~~~~~~~~~~~~~~~~-~~~~~~~~~~~~~~~~~##
# FUNCTIONS
#

### CONSTRUCTOR
def make_paddle(posX, posY, width, height):
    paddle = playground.create_rectangle(
        posX,           # X1
        posY,           # Y1
        posX + width,   # X2
        posY + height,  # Y2
        fill=SECONDARY_COLOR)
    return paddle

def make_ball(posX, posY, width):
    ball = playground.create_oval(
        posX,           # X1
        posY,           # Y1
        posX + width,   # X2
        posY + width,   # Y2
        fill=SECONDARY_COLOR)
    return ball

### GETTER
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

##~~~~~~~~~~~~~~~~-~~~~~~~~~~~~~~~~~##
# KEY BINDING
#
windows.bind("<Up>", lambda event: playground.move(right_paddle, 0, -5))
windows.bind("<Down>", lambda event: playground.move(right_paddle, 0, 5))
windows.bind("<z>", lambda event: playground.move(left_paddle, 0, -5))
windows.bind("<s>", lambda event: playground.move(left_paddle, 0, 5))
windows.bind("<Escape>", lambda event: windows.destroy())

""" Infinite loop won't work as it's tk.mainloop() job.
--- You should turn this into a function and call it with
--- windows.after(0, name_of_your_function_without_parenthesis)
--- this goes just before tk.mainloop in # main #.
---------------------------------------------
while True:
    if int(playground.coords(ball)[0]) > 200:
        playground.move(ball, DX, DY)
        print(playground.coords(ball))
"""

##~~~~~~~~~~~~~~~~-~~~~~~~~~~~~~~~~~##
# MAIN
#
### INIT
list_paddle.append(make_paddle(0, 0, paddle_width, paddle_height)) # Add a new paddle to the game
print(playground.coords(list_paddle[0]))
print(playground.bbox(list_paddle[0]))

list_ball.append(make_ball(100, 0, ball_width))
print(playground.coords(list_ball[0]))
print(playground.bbox(list_ball[0]))

### MAIN LOOP
"""-- windows.after() goes here --"""
windows.mainloop()
