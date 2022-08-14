from turtle import Screen
import time
from snake import Snake
from food import Food
from score_board import ScoreBoard
screen = Screen()

screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0)
snake = Snake()
food = Food()
score_board = ScoreBoard()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")


is_game_on = True
while is_game_on:
    screen.update()
    time.sleep(0.1)
    snake.move()
    # collision with food
    if snake.head.distance(food) < 15:
        score_board.increase_score()
        snake.add_segment()
        food.refresh()

    # collision with walls.
    if snake.head.xcor() > 297 or snake.head.xcor() < -280 or snake.head.ycor() > 297 or snake.head.ycor() < -297:
        is_game_on = False
        score_board.game_over()

    # collision with tail.
    for segment in snake.segment[1:]:
        if snake.head.distance(segment) < 10:
            is_game_on = False
            score_board.game_over()


screen.exitonclick()
