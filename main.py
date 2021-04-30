from turtle import Turtle, Screen
import random as r
import time as t
from snake import Snake
from score import ScoreBoard

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


def has_game_ended():
    if scr.onkeypress(fun=scr.exitonclick, key="e"):
        return True
    else:
        return snake.check_collision(scr)


while not has_game_ended():
    scr.update()
    snake.move()

    scr.onkeypress(fun=snake.right, key="Right")
    scr.onkeypress(fun=snake.left, key="Left")
    scr.onkeypress(fun=snake.up, key="Up")
    scr.onkeypress(fun=snake.down, key="Down")
    scr.onkeypress(fun=scr.exitonclick, key="e")

    t.sleep(0.1)

scr.exitonclick()
