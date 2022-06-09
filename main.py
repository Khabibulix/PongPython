import logging, random, math
import devconsole
import tkinter as tk

#Logging config
logging.basicConfig(filename="log.txt", filemode="w", level=logging.DEBUG)

score_a = 0
score_b = 0

#windows
windows = tk.Tk()
windows.title('Pong Game On Steroids')
windows.geometry("800x600")
windows.configure(bg="black")

#scoring
scoring = tk.Label(
    windows,
    text=f"Player A:\t{score_a}\t\t\t Player B:\t{score_b}",
    foreground="white",
    background="black",
    )
scoring.pack(ipadx=10, ipady=10)

windows.mainloop()