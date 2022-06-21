from turtle import Turtle

X = -430


class FirstPaddle:

    def __init__(self):
        self.y = 0
        self.paddle_one = Turtle("square")
        self.paddle_one.color("white")
        self.paddle_one.penup()
        self.paddle_one.turtlesize(stretch_wid=5, stretch_len=.5)
        self.paddle_one.goto(X, self.y)

    def move_up(self):
        self.y = self.y + 20
        self.paddle_one.goto(X, self.y)

    def move_down(self):
        self.y = self.y - 20
        self.paddle_one.goto(X, self.y)
