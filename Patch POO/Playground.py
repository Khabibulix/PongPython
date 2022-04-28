import turtle


score_a = 0
score_b = 0


class Pen():

    def initialisation(self):
        Pen = turtle.Turtle()
        Pen.speed(0)
        Pen.color("white")
        Pen.penup()
        Pen.hideturtle()
        Pen.goto(0, 260)
        Pen.write("Player A: 0\tPlayer B: 0", align="center", font=("Courier", 24, "normal"))


class Screen():
    
    def initialisation(self):
        Screen = turtle.Screen()
        Screen.title("Pong Me If You Can")
        Screen.bgcolor("black")
        Screen.setup(width=800, height=600)
        Screen.tracer(0)
        Screen.listen()
    
def creating_playground():
    pen = Pen()
    pen.initialisation()
    screen = Screen()
    screen.initialisation()

