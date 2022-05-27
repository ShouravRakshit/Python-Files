import random
import turtle

from turtle import Turtle
turtle.colormode(255)
tim = Turtle()
tim.speed("fast")
direction = [90,  270]
tim.pensize(5)

def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    random_color = (r, g, b)
    return random_color


while True:
    move = random.choice(direction)
    tim.forward(40)
    tim.color(random_color())
    tim.left(move)