import ElementMobile
import ElementStatique
import turtle
import winsound

#Score

score_a = 0
score_b = 0


#Functions

def leftPaddleGoingUp():
	y = leftPaddle.ycor()
	y += 20
	leftPaddle.sety(y)

def leftPaddleGoingDown():
	y = leftPaddle.ycor()
	y -= 20
	leftPaddle.sety(y)

def rightPaddleGoingUp():
	y = rightPaddle.ycor()
	y += 20
	rightPaddle.sety(y)

def rightPaddleGoingDown():
	y = rightPaddle.ycor()
	y -= 20
	rightPaddle.sety(y)

#Keyboard Input

screen.listen()
screen.onkeypress(leftPaddleGoingUp, "z")
screen.onkeypress(leftPaddleGoingDown, "s")
screen.onkeypress(rightPaddleGoingUp, "Up")
screen.onkeypress(rightPaddleGoingDown, "Down")

#Main game

while True:
	turtle.update()

	# Move the ball

	ball.setx(ball.xcor() + ball.dx)
	ball.sety(ball.ycor() + ball.dy)

	# Bouncing on borders

	# 290 car height de l'écran(600)/2 - height de la balle
	if ball.ycor() > 290:
		# inverse direction de la balle
		ball.sety(290)
		ball.dy *= -1
		winsound.PlaySound("pong.wav", winsound.SND_ASYNC)
	
	if ball.ycor() < -290:
		ball.sety(-290)
		ball.dy *= -1
		winsound.PlaySound("pong.wav", winsound.SND_ASYNC)

	if ball.xcor() > 390:
		ball.goto(0, 0)
		ball.dx *= -1
		score_a += 1
		pen.clear()
		pen.write("Player A: {} \tPlayer B: {}".format(score_a, score_b), align="center", font=("Courier", 24, "normal"))

	if ball.xcor() < -390:
		ball.goto(0, 0)
		ball.dx *= -1
		score_b += 1
		pen.clear()
		pen.write("Player A: {} \tPlayer B: {}".format(score_a, score_b), align="center", font=("Courier", 24, "normal"))

	# Collision detection
	# 340 car position du paddle - sa largeur
	# les ycor correspondent à la détection du paddle
	# seconde assertion pour éviter le glicht chelou entre le bord du screen et le paddle
	if ball.xcor() >  340 and ball.xcor() < 350 and ball.ycor() < rightPaddle.ycor() + 40 and ball.ycor() > rightPaddle.ycor() - 40:
		ball.setx(340)
		ball.dx *= -1
		winsound.PlaySound("pong.wav", winsound.SND_ASYNC)

	if ball.xcor() <  -340 and ball.xcor() > -350 and ball.ycor() > leftPaddle.ycor() - 40 and ball.ycor() < leftPaddle.ycor() + 40:
		ball.setx(-340)
		ball.dx *= -1
		winsound.PlaySound("pong.wav", winsound.SND_ASYNC)





