from turtle import Turtle, Screen

screen = Screen()
screen.tracer(0)

screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("PONG")

paddle = Turtle(shape="square")
paddle.color("white")
paddle.penup()
paddle.shapesize(stretch_wid=5, stretch_len=1)
paddle.goto(350, 0)


def up():
    new_y = paddle.ycor() + 20
    paddle.goto(paddle.xcor(), new_y)


def down():
    new_y = paddle.ycor() - 20
    paddle.goto(paddle.xcor(), new_y)


screen.listen()
screen.onkey(fun=up, key="Up")

screen.onkey(down, "Down")
game_is_on = True
while game_is_on:
    screen.update()

screen.exitonclick()
