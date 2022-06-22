from turtle import Turtle


class Level(Turtle):

    def __init__(self):
        super().__init__()
        self.color("red")
        self.penup()
        self.goto(-250, 250)
        self.hideturtle()
        self.current_level = 1
        self.level_up()

    def level_up(self):
        self.clear()
        self.write(f"Level {self.current_level}", font=("Arial", 20, "normal"))
        self.current_level += 1

