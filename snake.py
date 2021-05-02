from turtle import Turtle

UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0
MOVEMENT_SPEED = 20


class Snake:

    def __init__(self):
        self.snake_parts = []

    def create_snake(self):
        for _ in range(0, 3):
            self.snake_parts.append(Turtle("square"))
            self.snake_parts[_].penup()
            self.snake_parts[_].color("white")
            self.snake_parts[_].goto(20, 0)
            self.snake_parts[_].setx(self.snake_parts[_ - 1].position()[0] - 20)

    def right(self):
        if self.snake_parts[0].heading() != LEFT:
            self.snake_parts[0].setheading(RIGHT)

    def left(self):
        if self.snake_parts[0].heading() != RIGHT:
            self.snake_parts[0].setheading(LEFT)

    def up(self):
        if self.snake_parts[0].heading() != DOWN:
            self.snake_parts[0].setheading(UP)

    def down(self):
        if self.snake_parts[0].heading() != UP:
            self.snake_parts[0].setheading(DOWN)

    # TODO 2. Collision is missing for body collision.
    # TODO 4. Collision happening does not end the game appropriately, make more user friendly
    def check_collision(self, screen):
        if self.snake_parts[0].position()[0] >= screen.window_width() / 2 - 10:
            return True
        elif self.snake_parts[0].position()[0] <= (screen.window_width() / 2 - 10) * -1:
            return True
        elif self.snake_parts[0].position()[1] >= screen.window_height() / 2 - 20:
            return True
        elif self.snake_parts[0].position()[1] <= (screen.window_height() / 2 - 10) * -1:
            return True
        else:
            return False

    def grow_snake(self):
        snake_piece = Turtle("square")
        snake_piece.color("white")
        snake_piece.penup()
        current_last_piece = self.snake_parts[len(self.snake_parts) - 1]

        if self.snake_parts[0].heading() == RIGHT:
            snake_piece.setx(current_last_piece.xcor() - 20)
            snake_piece.setx(current_last_piece.ycor())
            self.snake_parts.append(snake_piece)
        elif self.snake_parts[0].heading() == LEFT:
            snake_piece.setx(current_last_piece.xcor() + 20)
            snake_piece.setx(current_last_piece.ycor())
            self.snake_parts.append(snake_piece)
        elif self.snake_parts[0].heading() == UP:
            snake_piece.setx(current_last_piece.xcor())
            snake_piece.setx(current_last_piece.ycor() - 20)
            self.snake_parts.append(snake_piece)
        elif self.snake_parts[0].heading() == DOWN:
            snake_piece.setx(current_last_piece.xcor())
            snake_piece.setx(current_last_piece.ycor() + 20)
            self.snake_parts.append(snake_piece)

    def move(self):
        for part_num in range(len(self.snake_parts) - 1, 0, -1):
            self.snake_parts[part_num].goto(self.snake_parts[part_num - 1].xcor(),
                                            self.snake_parts[part_num - 1].ycor())
        self.snake_parts[0].forward(MOVEMENT_SPEED)
