import logging, random, math
import devconsole
import tkinter as tk

#Logging config
logging.basicConfig(filename="log.txt", filemode="w", level=logging.DEBUG)

#global variables
DEFAULT_WIDTH = 800
DEFAULT_HEIGHT = 600

RIGHT_PADDLE_X = 780
LEFT_PADDLE_X = 10
PADDLE_Y = DEFAULT_HEIGHT/2
PADDLE_LENGTH = 200

PRIMARY_COLOR = "black"
SECONDARY_COLOR = "white"

BALL_X = 375
BALL_Y = 275

DY = 10
DX = 10

score_a = 0
score_b = 0


#windows
windows = tk.Tk()
windows.title('Pong Game On Steroids')
windows.geometry(str(DEFAULT_WIDTH)+"x"+str(DEFAULT_HEIGHT))
windows.configure(bg=PRIMARY_COLOR)
windows.resizable(False,False)

#scoring
scoring = tk.Label(
    windows,
    text=f"Player A: {score_a}\t\tPlayer B: {score_b}",
    foreground=SECONDARY_COLOR,
    background=PRIMARY_COLOR,
    font="consolas"
    )
scoring.pack(ipady=10)

#canvas
playground = tk.Canvas(windows,
    width=DEFAULT_WIDTH,
    height=DEFAULT_HEIGHT,
    bg=PRIMARY_COLOR
    )
playground.pack()

#paddle creation
left_paddle = playground.create_rectangle(
    LEFT_PADDLE_X,
    DEFAULT_HEIGHT/2,
    LEFT_PADDLE_X + 10,
    PADDLE_LENGTH,
    fill=SECONDARY_COLOR)
right_paddle = playground.create_rectangle(
    RIGHT_PADDLE_X,
    DEFAULT_HEIGHT/2,
    RIGHT_PADDLE_X - 10,
    PADDLE_LENGTH,
    fill=SECONDARY_COLOR)
"""
create_rectangle(x,y,x2,y2)
    (x,y) is the defaults coodinates before tracing
    (x2,y2) is the defaults coodinates after tracing
"""

#ball creation
ball = playground.create_oval(
    BALL_X,
    BALL_Y,
    BALL_X + 10,
    BALL_Y + 10,
    fill=SECONDARY_COLOR)

#keybinding
windows.bind("<Up>", lambda event: playground.move(right_paddle, 0, -5))
windows.bind("<Down>", lambda event: playground.move(right_paddle, 0, 5))
windows.bind("<z>", lambda event: playground.move(left_paddle, 0, -5))
windows.bind("<s>", lambda event: playground.move(left_paddle, 0, 5))
windows.bind("<Escape>", lambda event: windows.destroy())

while True:
    if int(playground.coords(ball)[0]) > 200:
        playground.move(ball, DX, DY)
        print(playground.coords(ball))


windows.mainloop()
