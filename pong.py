# Pong GUI game using turtle Python 3
# Saffian Baig

import turtle
import winsound

window = turtle.Screen()
window.title("Pong by Sufi")
window.bgcolor("black")
window.setup(width=1280, height=720)
window.tracer(0) # Update the windows manually

# Player A Padel
paddle_a = turtle.Turtle()
paddle_a.speed(0)
paddle_a.shape("square")
paddle_a.color("white")
paddle_a.shapesize(stretch_wid=5, stretch_len=1)
paddle_a.penup()  # turtle draws lines as it moves , this prevents that
paddle_a.goto(-590,0)   # start paddle at this


# Player B Padel  
paddle_b = turtle.Turtle()
paddle_b.speed(0)
paddle_b.shape("square")
paddle_b.color("white")
paddle_b.shapesize(stretch_wid=5, stretch_len=1)
paddle_b.penup()  # turtle draws lines as it moves , this prevents that
paddle_b.goto(590,0)   # start paddle at this

# Ball
ball = turtle.Turtle()
ball.speed(0)
ball.shape("circle")
ball.color("white")
ball.penup()
ball.goto(0,0)
ball.dx = 0.2
ball.dy = 0.2

# move paddle a up
def paddle_a_up():
    y = paddle_a.ycor()
    y += 20
    paddle_a.sety(y)
    
# move paddle a down
def paddle_a_down():
    y = paddle_a.ycor()
    y -= 20
    paddle_a.sety(y)    

# move paddle b up
def paddle_b_up():
    y = paddle_b.ycor()
    y += 20
    paddle_b.sety(y)
    
# move paddle b down
def paddle_b_down():
    y = paddle_b.ycor()
    y -= 20
    paddle_b.sety(y)  
    
# Key binds for paddle a up

window.listen()
window.onkeypress(paddle_a_up,"w")
window.onkeypress(paddle_a_down,"s")
window.onkeypress(paddle_b_up,"Up")
window.onkeypress(paddle_b_down,"Down")

# Turtle Pen for making the points board
score_a = 0
score_b = 0
# Showing the board
pen = turtle.Turtle()
pen.speed(0)
pen.color("white")
pen.penup()
pen.hideturtle() # Just need the text, not the body of the turtle
pen.goto(0,260)
pen.write("Player A : 0     Player B : 0", align = "center" , font=("Calibri",26,"normal"))




while True:
    window.update()

    # Moving the ball
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    # What happens when the ball hits the border
    # Check when y value of ball compares to the height extremes of the window

    if (ball.ycor() > 350):
        ball.sety(350)
        ball.dy *= -1
        winsound.PlaySound("ball.mp3",winsound.SND_ASYNC)

    if (ball.ycor() < -350):
        ball.sety(-350)
        ball.dy *= -1
        winsound.PlaySound("ball.mp3",winsound.SND_ASYNC)
    
    if (ball.xcor() > 630):
        ball.goto(0,0)
        ball.dx *= -1
        score_a += 1
        pen.clear() # Clear up pen board so it doesnt overwrite
        pen.write("Player A : {}     Player B : {}".format(score_a,score_b), align = "center" , font=("Calibri",26,"normal"))


    if (ball.xcor() < -630):
        ball.goto(0,0)
        ball.dx *= -1
        score_b += 1
        pen.clear()
        pen.write("Player A : {}     Player B : {}".format(score_a,score_b), align = "center" , font=("Calibri",26,"normal"))


    # Now the ball colliding with the paddle

    if  (ball.xcor() > 570 and ball.xcor() < 590) and (ball.ycor() < paddle_b.ycor() + 50 and ball.ycor() > paddle_b.ycor() - 50):
        ball.setx(570)
        ball.dx *= -1 
    if  (ball.xcor() < -570 and ball.xcor() > -590) and (ball.ycor() < paddle_a.ycor() + 50 and ball.ycor() > paddle_a.ycor() - 50):
        ball.setx(-570)
        ball.dx *= -1 