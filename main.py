# import colorgram
#
# rgb_colors = []
# colors = colorgram.extract("image.jpg", 21)
# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     new_color = (r, g, b)
#     rgb_colors.append(new_color)
#
# print(rgb_colors)
import turtle
from turtle import Turtle, Screen
import random
turtle.colormode(255)
tim = Turtle()
tim.speed("fastest")
tim.penup()
tim.hideturtle()
color_list = [(236, 35, 108), (221,   232, 237), (145, 28, 64), (239, 75, 35), (6, 148, 93), (232, 238, 234),
              (231, 168, 40), (184, 158, 46), (44, 191, 233), (27, 127, 195), (126, 193, 74), (253, 223, 0),
              (85, 28, 93), (173, 36, 97), (246, 219, 44), (44, 172, 112), (215, 130, 165), (215, 56, 27),
              (235, 164, 191)]

tim.setheading(225)
tim.forward(300)
tim.setheading(0)
number_of_dots = 100
for dot_count in range(1, number_of_dots + 1):
    tim.dot(20, random.choice(color_list))
    tim.forward(50)
    if dot_count % 10 == 0:
        tim.setheading(90)
        tim.forward(50)
        tim.setheading(180)
        tim.forward(500)
        tim.setheading(0)

screen = Screen()
screen.exitonclick()

