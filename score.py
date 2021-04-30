from turtle import  Turtle


class ScoreBoard:
    player_score = 0

    def display_score(self):
        text_turtle = Turtle()
        text_turtle.penup()
        text_turtle.hideturtle()
        text_turtle.goto(0, 280)
        text_turtle.color("white")
        text_turtle.write(f"Player score: {self.player_score}", move=False, align="center",
                          font=("Arial", 14, "normal"))
