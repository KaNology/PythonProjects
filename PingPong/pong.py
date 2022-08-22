import turtle
import time
import simpleaudio as sa

wave_object = sa.WaveObject.from_wave_file('PingPong/HitSoundEffect.wav')
# play_object = wave_object.play()
# play_object.wait_done()

# Player Scores
score_A = 0
score_B = 0

# Screen Setup
screen = turtle.Screen()
screen.title("Ping Pong")
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.tracer(0)

# Paddle A (on the left side)
paddleA = turtle.Turtle()
paddleA.speed(0)
paddleA.shape("square")
paddleA.color("yellow")
# The default size of turtle object is 10 pixels.
# So with shapesize like bellow, the shape size should be width = 50, length = 10
paddleA.shapesize(stretch_wid=5,stretch_len=1)
paddleA.penup()
paddleA.goto(-350, 0)

# Paddle B (on the right side)
paddleB = turtle.Turtle()
paddleB.speed(0)
paddleB.shape("square")
paddleB.color("purple")
paddleB.shapesize(stretch_wid=5,stretch_len=1)
paddleB.penup()
paddleB.goto(350, 0)

# Ball
ball = turtle.Turtle()
ball.speed(1)
ball.shape("circle")
ball.color("white")
ball.shapesize(stretch_wid=1, stretch_len=1)
ball.penup()
ball.goto(0, 0)
ball.left(45)
ball_speed = 3
ball_x_dir, ball_y_dir = ball_speed, ball_speed
xlimit, ylimit = screen.window_width() / 2, screen.window_height() / 2

# The Heading
pen = turtle.Turtle()
pen.speed(0)
pen.shape("square")
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
pen.write(f"Lee An: {score_A}  LHN: {score_B}", align="center", font=("Courier", 24, "normal"))

def ball_motion():
    global ball_x_dir, ball_y_dir, score_A, score_B

    # When ball touches the upper side of the screen
    if ball.ycor() >= ylimit:
        ball_y_dir *= -1

    # When ball touches the bottom side of the screen
    if ball.ycor() <= -ylimit:
        ball_y_dir *= -1

    # When ball touches the right side of the screen
    if ball.xcor() >= xlimit:
        score_A += 1
        ball.goto(0, 0)
        ball_x_dir *= -1
        pen.clear()
        pen.write(f"Lee An: {score_A}  LHN: {score_B}", align="center", font=("Courier", 24, "normal"))
        return None

    # When ball touches the left side of the screen
    if ball.xcor() <= -xlimit:
        score_B += 1
        ball.goto(0, 0)
        ball_x_dir *= -1
        pen.clear()
        pen.write(f"Lee An: {score_A}  LHN: {score_B}", align="center", font=("Courier", 24, "normal"))

    # When the ball touches paddle A
    # Left side (no need cuz it'll just bounce back and the player loses)
    paddleA_right_x = paddleA.xcor() + (10 * 1) / 2
    paddleA_bot_y = paddleA.ycor() - (10 * 5) / 2
    paddleA_up_y = paddleA.ycor() + (10 * 5) / 2
    if ball.xcor() <= paddleA_right_x and ball.ycor() <= paddleA_up_y and ball.ycor() >= paddleA_bot_y:
        ball_x_dir *= -1

    # When the ball touches paddle B
    paddleB_left_x = paddleB.xcor() - (10 * 1) / 2
    paddleB_bot_y = paddleB.ycor() - (10 * 5) / 2
    paddleB_up_y = paddleB.ycor() + (10 * 5) / 2
    if ball.xcor() >= paddleB_left_x and ball.ycor() <= paddleB_up_y and ball.ycor() >= paddleB_bot_y:
        ball_x_dir *= -1
    
    ball.goto(ball.xcor() + ball_x_dir, ball.ycor() + ball_y_dir)

def paddleAUp():
    paddleA.sety(paddleA.ycor() + 10)

def paddleADown():
    paddleA.sety(paddleA.ycor() - 10)

def paddleBUp():
    paddleB.sety(paddleB.ycor() + 10)

def paddleBDown():
    paddleB.sety(paddleB.ycor() - 10)

def paddleBAI():
    if ball.xcor() >= 0:
        if ball.ycor() >= paddleB.ycor():
            paddleBUp()
        else:
            paddleBDown()

def paddleAAI():
    if ball.xcor() <= 0:
        if ball.ycor() >= paddleA.ycor():
            paddleAUp()
        else:
            paddleADown()

screen.listen()
screen.onkeypress(paddleAUp, 'w')
screen.onkeypress(paddleADown, 's')
screen.onkeypress(paddleBUp, 'Up')
screen.onkeypress(paddleBDown, 'Down')

while True:
    time.sleep(1 / 60000) # For a consistent ball movement
    ball_motion()
    paddleAAI()
    paddleBAI()
    screen.update()