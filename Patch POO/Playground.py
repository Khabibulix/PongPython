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
        Pen.write(""
                  "Player A: 0\t"
                  "Player B: 0",
                  align="center",
                  font=("Courier", 24, "normal")
                  )


class Screen:

    def initialisation(self, s):
        s = turtle.Screen()
        s.title("Pong Me If You Can")
        s.bgcolor("black")
        s.setup(width=800, height=600)
        s.tracer(0)
        s.listen()


pen = Pen()
pen.initialisation()
screen = Screen()
screen.initialisation(screen)
