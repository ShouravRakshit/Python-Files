import random
import turtle

from turtle import Turtle, Screen

turtle.colormode(255)
tim = Turtle()
tim.speed("fast")
tim.pensize(5)
direction = [0, 90, 180, 270]


def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    color = (r, g, b)
    return color


def draw():
    while True:
        tim.left(random.choice(direction))
        tim.color(random_color())
        tim.forward(30)
        if tim.xcor() >= 400 or tim.xcor() <= -400 or tim.ycor() >= 300 or tim.ycor() <= -300:
            break


draw()
screen = Screen()
print(screen.screensize())
screen.exitonclick()
