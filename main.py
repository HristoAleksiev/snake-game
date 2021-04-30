from turtle import Turtle, Screen
import random as r
import time as t
from snake import Snake
from score import ScoreBoard
from food import Food

scr = Screen()
scr.setup(width=600, height=600)
scr.bgcolor("black")
scr.title("Snake Game!")
scr.tracer(0)
scr.listen()

snake = Snake()
snake.create_snake()

score = ScoreBoard()
score.display_score()

food = Food()


def has_game_ended():
    if scr.onkeypress(fun=scr.exitonclick, key="e"):
        return True
    else:
        return snake.check_collision(scr)


while not has_game_ended():
    scr.update()

    if food.is_eaten(snake):
        food.recreate()
        score.update_score()
        snake.grow_snake()

    snake.move()

# onkey() or onkeypress() ??
    scr.onkey(fun=snake.right, key="Right")
    scr.onkey(fun=snake.left, key="Left")
    scr.onkey(fun=snake.up, key="Up")
    scr.onkey(fun=snake.down, key="Down")
    scr.onkey(fun=scr.exitonclick, key="e")

    t.sleep(0.1)

scr.exitonclick()
