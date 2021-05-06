from turtle import Screen
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
        if snake.check_collision(scr):
            score.check_high_score()
            return True


while not has_game_ended():
    if food.is_eaten(snake):
        food.recreate()
        score.update_score()
        snake.grow_snake()

    if scr.onkeypress(fun=snake.right, key="Right") or scr.onkeypress(fun=snake.left, key="Left") \
            or scr.onkeypress(fun=snake.up, key="Up") or scr.onkeypress(fun=snake.down, key="Down") \
            or scr.onkeypress(fun=scr.exitonclick, key="e"):
        pass
    snake.move()
    scr.update()

    t.sleep(0.1)

scr.exitonclick()
