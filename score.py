from turtle import  Turtle


class ScoreBoard:

    def __init__(self):
        self.player_score = 0
        self.text_turtle = Turtle()

    def display_score(self):
        self.text_turtle.penup()
        self.text_turtle.hideturtle()
        self.text_turtle.goto(0, 280)
        self.text_turtle.color("white")
        self.text_turtle.write(f"Player score: {self.player_score}", move=False, align="center",
                          font=("Arial", 14, "normal"))

    def update_score(self):
        self.player_score += 1
        self.text_turtle.clear()
        self.text_turtle.write(f"Player score: {self.player_score}", move=False, align="center",
                               font=("Arial", 14, "normal"))
