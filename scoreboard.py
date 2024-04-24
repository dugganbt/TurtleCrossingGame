FONT = ("Courier", 24, "normal")
from turtle import Turtle


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.goto(-220, 250)
        self.level = 1
        self.update_scoreboard()

    def increase_level(self):
        self.level += 1
        self.update_scoreboard()

    def display_game_over(self):
        self.goto(0,0)
        self.write("GAME OVER.", align="center", font=FONT)

    def update_scoreboard(self):
        self.clear()
        self.write(f"Level: {self.level}", align="center", font=FONT)