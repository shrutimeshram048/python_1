from turtle import Turtle


class Paddle:
    paddle = Turtle(shape="square")
    paddle.color("white")
    paddle.penup()
    paddle.shapesize(stretch_wid=5, stretch_len=1)

    def co(self, ):