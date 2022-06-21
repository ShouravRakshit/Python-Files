from turtle import Turtle


class ScoreBoard(Turtle):

    def __init__(self):
        super().__init__()
        self.goto(-50, 250)
        self.color("white")
        self.hideturtle()
        self.player_one_score = 0
        self.player_two_score = 0
        self.write(f"{self.player_one_score} \t {self.player_two_score}", font=("Arial", 15, "normal"))

    # Increasing the score for the first paddle
    def paddle_one_score(self):
        self.clear()
        self.player_one_score += 1
        self.write(f"{self.player_one_score} \t {self.player_two_score}", font=("Arial", 15, "normal"))

    # Increasing the score for the second paddle
    def paddle_two_score(self):
        self.clear()
        self.player_two_score += 1
        self.write(f"{self.player_one_score} \t {self.player_two_score}", font=("Arial", 15, "normal"))
