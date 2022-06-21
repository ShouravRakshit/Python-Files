from turtle import Turtle


class Ball:

    def __init__(self, position):
        self.pong_ball = Turtle("circle")
        self.pong_ball.speed(1)
        self.pong_ball.goto(position)
        self.pong_ball.penup()
        self.pong_ball.color("black")
        self.x_increase = 10
        self.y_increase = 10

    def move(self):
        x_coor = self.pong_ball.xcor() + self.x_increase
        y_coor = self.pong_ball.ycor() + self.y_increase
        self.pong_ball.goto(x_coor, y_coor)

    def bounce_back(self):
        self.y_increase = self.y_increase - 10

