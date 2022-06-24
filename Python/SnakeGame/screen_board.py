from turtle import Turtle

FONT = ("Arial", 15, "normal")


# This class is showing the score of the player.
class Score:

    def __init__(self):
        self.title = Turtle()
        self.title.penup()
        self.title.hideturtle()
        self.score = 0
        with open("data.txt", mode="r") as file:
            self.high_score = int(file.read())

        self.title.speed(0)
        self.title.color("white")
        self.title.goto(-70, 250)
        self.increase_score()

    # Score increase method.
    def increase_score(self):
        self.title.clear()
        if self.score > self.high_score:
            self.high_score = self.score
            with open("data.txt", mode="w") as file:
                file.write(f"{self.high_score}")
        self.title.write(f"Score : {self.score} High Score: {self.high_score}", font=FONT)
        self.score += 1

    # This method will run if the game is over.
    def game_over(self):
        self.title.goto(0, 0)
        self.title.write(f"GAME OVER", font=FONT, align="center")