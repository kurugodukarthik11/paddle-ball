import turtle

w = turtle.Screen()
w.title("PADDLE_BALL")
w.bgcolor("#0A0A0A")
w.setup(width=800, height=600)
w.tracer(0)

p = turtle.Turtle()
p.width(8)
p.pencolor('#F7EE01')
p.penup()
p.goto(0, 300)
p.pendown()
p.goto(0, -300)
p.penup()

paddle_1 = turtle.Turtle()
paddle_1.shape("square")
paddle_1.speed(0)
paddle_1.shapesize(stretch_wid=4, stretch_len=0.7)
paddle_1.color("white")
paddle_1.penup()
paddle_1.goto(-390, 0)  # -390

paddle_2 = turtle.Turtle()
paddle_2.shape("square")
paddle_2.speed(0)
paddle_2.shapesize(stretch_wid=4, stretch_len=0.7)
paddle_2.color("white")
paddle_2.penup()
paddle_2.goto(380, 0)  # 380

ball = turtle.Turtle()
ball.speed(0)
ball.shape("circle")
ball.color("white")
ball.penup()
ball.goto(0, 0)

# speed of the ball

ball.px = 0.1
ball.py = 0.1

# scores

player_1 = 0
player_2 = 0

pen = turtle.Turtle()
pen.speed(0)
pen.shape("square")
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
pen.write("Player A: 0  Player B: 0", align="center", font=("Monospace", 20, "bold"))


def paddle_1_up():
    y = paddle_1.ycor()
    y += 15
    paddle_1.sety(y)
    if paddle_1.ycor() > 248:
        paddle_1.sety(248)


def paddle_2_up():
    y = paddle_2.ycor()
    y += 15
    paddle_2.sety(y)
    if paddle_2.ycor() > 248:
        paddle_2.sety(248)


def paddle_1_down():
    y = paddle_1.ycor()
    y -= 15
    paddle_1.sety(y)
    if paddle_1.ycor() < -240:
        paddle_1.sety(-240)


def paddle_2_down():
    y = paddle_2.ycor()
    y -= 15
    paddle_2.sety(y)
    if paddle_2.ycor() < -240:
        paddle_2.sety(-240)


w.listen()
w.onkeypress(paddle_1_up, "w")
w.onkeypress(paddle_1_up, "W")
w.onkeypress(paddle_2_up, "Up")
w.onkeypress(paddle_1_down, "s")
w.onkeypress(paddle_1_down, "S")
w.onkeypress(paddle_2_down, "Down")

win = True
while win:
    w.update()
    ball.setx(ball.xcor() + ball.px)
    ball.sety(ball.ycor() + ball.py)

    if ball.ycor() >= 286:
        ball.sety(286)
        ball.py *= -1
    elif ball.ycor() <= -280:
        ball.sety(-280)
        ball.py *= -1

    if ball.xcor() >= 380:
        player_1 += 1
        pen.clear()
        pen.write("Player A: {}  Player B: {}".format(player_1, player_2), align="center",
                  font=("Monospace", 20, "bold"))
        ball.goto(0, 0)
        ball.px *= -1

    elif ball.xcor() <= -387:
        player_2 += 1
        pen.clear()
        pen.write("Player A: {}  Player B: {}".format(player_1, player_2), align="center",
                  font=("Monospace", 20, "bold"))
        ball.goto(0, 0)
        ball.px *= -1

    if (360 < ball.xcor() < 370) and (paddle_2.ycor() + 50 > ball.ycor() > paddle_2.ycor() - 50):
        ball.setx(340)
        ball.px *= -1
    if (-380 < ball.xcor() < -370) and (paddle_1.ycor() + 50 > ball.ycor() > paddle_1.ycor() - 50):
        ball.setx(-340)
        ball.px *= -1

    if player_1 == 10 or player_2 == 10:

        if player_1 > player_2:
            pen.clear()
            pen.write("Player 1 wins", align="center",
                      font=("Monospace", 20, "bold"))
            print("Player 1 wins")

        else:
            pen.clear()
            pen.write("Player 2 wins", align="center",
                      font=("Monospace", 20, "bold"))
            print("PLayer 2 wins")

        win = False
