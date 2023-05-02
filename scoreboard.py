from turtle import Turtle

class Scoreboard(Turtle):

    SCORE = 1

    ALIGNMENT = "center"

    FONT = ("Courier", 12, "bold")

    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.goto(250, 300)
        self.update_score()

    def update_score(self):
        self.clear()
        self.write(f"LEVEL: {self.SCORE}", align=self.ALIGNMENT, font=self.FONT)

    def game_over(self):
        self.clear()
        self.goto(0, 0)
        self.write(f"GAME OVER", align=self.ALIGNMENT, font=self.FONT)