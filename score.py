from turtle import Turtle, Screen
from highscores import high_scores


class ScoreBoard:

    def __init__(self):
        self.player_score = 0
        self.text_turtle = Turtle()
        self.screen = Screen()
        # to be a read/write from a text file and allow high scores to transcend to other runs of the program
        self.high_scores = high_scores

    def display_score(self):
        self.text_turtle.penup()
        self.text_turtle.hideturtle()
        self.text_turtle.goto(0, 280)
        self.text_turtle.color("red")
        self.text_turtle.write(f"Player score: {self.player_score}", move=False, align="center",
                               font=("Arial", 14, "normal"))

    def update_score(self):
        self.player_score += 1
        self.text_turtle.clear()
        self.text_turtle.write(f"Player score: {self.player_score}", move=False, align="center",
                               font=("Arial", 14, "normal"))

    def check_high_score(self):
        if self.player_score > self.high_scores[len(self.high_scores) - 1][1]:
            player_name = self.screen.textinput("High score detected!",
                                                "What name should we record the high score under?")
            self.order_high_scores(player_name)
        self.display_high_scores()

    # this is weird, could be written cleaner
    def order_high_scores(self, name):
        x = 0
        for score in range(len(self.high_scores) - 1, -1, -1):
            if self.high_scores[score][1] < self.player_score:
                x = self.high_scores[score]
                self.high_scores[score] = (name, self.player_score)
                if score + 1 <= len(self.high_scores) - 1:
                    self.high_scores[score + 1] = x

    def display_high_scores(self):
        turtle_x = 0
        turtle_y = 0
        self.text_turtle.goto(turtle_x, turtle_y)
        self.text_turtle.write(arg=f" Game Over!\nFinal score: {self.player_score}", align="center",
                               font=("Arial", 16, "normal"))
        turtle_y -= 40
        self.text_turtle.goto(turtle_x, turtle_y)
        self.text_turtle.write(arg=f" HIGH SCORES!", align="center", font=("Arial", 20, "normal"))
        for hscore in self.high_scores:
            turtle_y -= 20
            self.text_turtle.goto(turtle_x, turtle_y)
            self.text_turtle.write(arg=f" {hscore[0]}: {hscore[1]}", align="center",
                                   font=("Arial", 16, "normal"))
