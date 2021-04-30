from turtle import Turtle
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake:
    snake_parts = []

# TODO 3. The snake should become bigger when ingesting food.
    def create_snake(self):
        for _ in range(0, 3):
            self.snake_parts.append(Turtle("square"))
            self.snake_parts[_].penup()
            self.snake_parts[_].color("white")
            self.snake_parts[_].goto(20, 0)
            self.snake_parts[_].setx(self.snake_parts[_ - 1].position()[0] - 20)

    def right(self):
        if self.snake_parts[0].heading() != LEFT:
            self.snake_parts[0].setheading(0)

    def left(self):
        if self.snake_parts[0].heading() != RIGHT:
            self.snake_parts[0].setheading(180)

    def up(self):
        if self.snake_parts[0].heading() != DOWN:
            self.snake_parts[0].setheading(90)

    def down(self):
        if self.snake_parts[0].heading() != UP:
            self.snake_parts[0].setheading(270)

# TODO 2. Collision is missing for body and food collision.
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

    def move(self):
        for part_num in range(len(self.snake_parts) - 1, 0, -1):
            self.snake_parts[part_num].goto(self.snake_parts[part_num - 1].xcor(),
                                            self.snake_parts[part_num - 1].ycor())
        self.snake_parts[0].forward(20)
