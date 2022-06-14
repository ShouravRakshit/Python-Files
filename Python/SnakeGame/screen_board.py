from turtle import Turtle

FONT = ("Arial", 25, "normal")


# This class is showing the score of the player.
class Score:

    def __init__(self):
        self.title = Turtle()
        self.title.penup()
        self.title.hideturtle()
        self.score = 0
        self.title.speed(0)
        self.title.color("white")
        self.title.goto(-70, 250)
        self.increase_score()

    # Score increase method.
    def increase_score(self):
        self.title.clear()
        self.title.write(f"Score : {self.score}", font=FONT)
        self.score += 1

    # This text will show up if the game is over.
    def game_over(self):
        self.title.goto(0, 0)
        self.title.write(f"GAME OVER", font=FONT, align="center")