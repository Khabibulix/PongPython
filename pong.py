
#Import and Setup

import turtle

screen = turtle.Screen()
screen.title("Pong Me If You Can")
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.tracer(0)

#Paddle 1

leftPaddle = turtle.Turtle()
leftPaddle.speed(0)
leftPaddle.shape("square")
leftPaddle.color("white")
leftPaddle.shapesize(stretch_wid=5, stretch_len=1)
leftPaddle.penup()
leftPaddle.goto(-350, 0)

#Paddle 2

rightPaddle = turtle.Turtle()
rightPaddle.speed(0)
rightPaddle.shape("square")
rightPaddle.color("white")
rightPaddle.shapesize(stretch_wid=5, stretch_len=1)
rightPaddle.penup()
rightPaddle.goto(350, 0)

#Ball

ball = turtle.Turtle()
ball.speed(0)
ball.shape("turtle")
ball.color("white")
ball.penup()
ball.goto(0, 0)
ball.dx = 1
ball.dy = 1


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

	#Bouncing on borders

	# 290 car height de l'écran(600)/2 - height de la balle
	if ball.ycor() > 290:
		#inverse direction de la balle
		ball.sety(290)
		ball.dy *= -1
	
	if ball.ycor() < -290:
		ball.sety(-290)
		ball.dy *= -1

	if ball.xcor() > 390:
		ball.goto(0)
		ball.dx *= -1





