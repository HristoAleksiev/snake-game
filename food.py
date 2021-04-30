import random as r
from turtle import Turtle


class Food:

    def __init__(self):
        self.food_piece = Turtle("circle")
        self.spawn()

    def spawn(self):
        random_x = r.randrange(-280, 280, 20)
        random_y = r.randrange(-280, 260, 20)

        self.food_piece.shapesize(0.4)
        self.food_piece.color("pink")
        self.food_piece.penup()
        self.food_piece.goto(random_x, random_y)

# Snake movement generates insanely small residue of the likes of 0.0000000000003, must round in comparison for the code
# to work as intended!
    def is_eaten(self, snake):
        if round(snake.snake_parts[0].position()[1]) == self.food_piece.position()[1] and \
                round(snake.snake_parts[0].position()[0]) == self.food_piece.position()[0]:
            return True
        else:
            return False

    def recreate(self):
        random_x = r.randrange(-280, 280, 20)
        random_y = r.randrange(-280, 260, 20)

        self.food_piece.goto(random_x, random_y)

# TODO: 1. Build the main food spawn for the snake
