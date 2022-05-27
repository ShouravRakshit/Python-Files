from turtle import Turtle, Screen
import random
import turtle


def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    random_rgb = (r, g, b)
    return random_rgb


tim = Turtle()
turtle.colormode(255)


def draw_shape():
    side = 3
    while True:
        tim.color(random_color())
        for i in range(side):
            tim.forward(100)
            tim.right(360 / side)
        side += 1
        if side == 11:
            break


draw_shape()

screen = Screen()
screen.exitonclick()
