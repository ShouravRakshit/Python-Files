from turtle import Turtle


class Player:

    def __init__(self):
        self.player = Turtle("turtle")
        self.player.penup()
        self.player.goto(0, -280)
        self.player.setheading(90)

    def move_up(self):
        self.player.forward(15)

    def move_left(self):
        self.player.goto(self.player.xcor() - 15, self.player.ycor())

    def move_right(self):
        self.player.goto(self.player.xcor() + 15, self.player.ycor())

    def move_down(self):
        self.player.backward(15)

    def reset(self):
        self.player.goto(0, -280)
