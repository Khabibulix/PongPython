import turtle

class ElementStatique:
    def screen_init(self):
        screen = turtle.Screen()
        screen = turtle.Screen()
        screen.title("Pong Me If You Can")
        screen.bgcolor("black")
        screen.setup(width=800, height=600)
        screen.tracer(0)
        # rebond sur bordures en méthode


class Score(ElementStatique):

    def score_init(self, score):
        score = turtle.Turtle()
        score.speed(0)
        score.color("white")
        score.penup()
        score.hideturtle()
        score.goto(positionX=0, positionY=260)
        score.write("Player A: 0\tPlayer B: 0", align="center", font=("Courier", 24, "normal"))

