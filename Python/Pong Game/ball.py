from turtle import Turtle


class Ball:

    def __init__(self, position):
        self.pong_ball = Turtle("circle")
        self.pong_ball.speed(1)
        self.pong_ball.goto(position)
        self.pong_ball.penup()
        self.pong_ball.color("white")
        self.x_increase = 10
        self.y_increase = 10

    def move(self):
        x_coordinate = self.pong_ball.xcor() + self.x_increase
        y_coordinate = self.pong_ball.ycor() + self.y_increase
        self.pong_ball.goto(x_coordinate, y_coordinate)

    def wall_bounce(self):
        self.y_increase = self.y_increase * (-1)

    def paddle_bounce(self):
        self.x_increase = self.x_increase * (-1)

    # reset the position of the ball if one of the paddle scores.
    def reset_ball(self):
        self.pong_ball.goto(0, 0)

