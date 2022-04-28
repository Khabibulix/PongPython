import winsound


#borders variables for more lisibility
up_border = 290
down_border = -290
right_goal = 390
left_goal = -390

#intern logic
def importing_logic():
    ball_touching_right_paddle = ball.xcor() < -340 and ball.xcor() > -350
    ball_on_top_or_bottom_right_paddle = ball.ycor < rightPaddle.ycor() + 40 and ball.ycor() > rightPaddle.ycor() - 40
    ball_touching_left_paddle = ball.xcor() > 340 and ball.xcor() < 350
    ball_on_top_or_bottom_left_paddle = ball.ycor() > leftPaddle.ycor() - 40 and ball.ycor() < leftPaddle.ycor() + 40



class Ball():
    def __init__(self, speed=int, shape=str, color=str):
        speed = self.speed
        shape= self.shape
        color = self.color

    def initialisation(self):
        Ball = turtle.Turtle()
        Ball.shapesize(0.7, 0.7)
        Ball.penup()
        Ball.goto(0, 0)
        Ball.dx = 0.25
        Ball.dy = 0.25

    def moving_ball(self):
        Ball.setx(Ball.xcor() + Ball.dx)
        Ball.sety(Ball.ycor() + Ball.dy)

    def collision_detection(self):
        importing_logic()
        if ball.ycor() > up_border:
            # inverse direction de la balle
            ball.sety(up_border)
            ball.dy *= -1
            winsound.PlaySound("pong.wav", winsound.SND_ASYNC)

        if ball.ycor() < down_border:
            ball.sety(down_border)
            ball.dy *= -1
            winsound.PlaySound("pong.wav", winsound.SND_ASYNC)

        if ball.xcor() > right_goal:
            ball.goto(0, 0)
            ball.dx *= -1
            score_a += 1
            pen.clear()
            pen.write("Player A: {} \tPlayer B: {}".format(score_a, score_b), align="center",
                      font=("Courier", 24, "normal"))

        if ball.xcor() <left_goal:
            ball.goto(0, 0)
            ball.dx *= -1
            score_b += 1
            pen.clear()
            pen.write("Player A: {} \tPlayer B: {}".format(score_a, score_b), align="center",
                      font=("Courier", 24, "normal"))

        if ball_touching_right_paddle and ball_on_top_or_bottom_right_paddle:
            ball.setx(340)
            ball.dx *= -1
            winsound.PlaySound("pong.wav", winsound.SND_ASYNC)

        if  ball_touching_left_paddle and ball_on_top_or_bottom_left_paddle:
            ball.setx(-340)
            ball.dx *= -1
            winsound.PlaySound("pong.wav", winsound.SND_ASYNC)

def creating_ball():
    ball = Ball(speed=0, shape="circle", color="white")
    Ball.initialisation()
    Ball.moving_ball()
