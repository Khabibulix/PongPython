import logging, random, math
import devconsole
import tkinter as tk

#Logging config
logging.basicConfig(filename="log.txt", filemode="w", level=logging.DEBUG)

DEFAULT_WIDTH = 800
DEFAULT_HEIGHT = 600
score_a = 0
score_b = 0

#TODO jouer avec les padding pour centrer la fenêtre (winfo_screen)
#windows
windows = tk.Tk()
windows.title('Pong Game On Steroids')
windows.geometry(str(DEFAULT_WIDTH)+"x"+str(DEFAULT_HEIGHT))
windows.configure(bg="black")
windows.resizable(False,False)

#scoring
scoring = tk.Label(
    windows,
    text=f"Player A: {score_a}\t\tPlayer B: {score_b}",
    foreground="white",
    background="black",
    font="consolas"
    )
scoring.pack(ipady=10)

#canvas
playground = tk.Canvas(windows,
    width=DEFAULT_WIDTH,
    height=DEFAULT_HEIGHT,
    bg="black"
    )

#paddle creation
left_paddle = playground.create_rectangle(10, DEFAULT_HEIGHT/2, 20, 200, fill="white")
right_paddle = playground.create_rectangle(780, DEFAULT_HEIGHT/2, 790, 200, fill="white")
"""
create_rectangle(x,y,x2,y2)
    (x,y) is the defaults coodinates before tracing
    (x2,y2) is the defaults coodinates after tracing
"""

#ball creation
ball = playground.create_oval(375,275,385,285,fill="white")

playground.pack()


windows.mainloop()