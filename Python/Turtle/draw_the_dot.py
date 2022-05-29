import colorgram
import random
from turtle import Turtle, Screen
import turtle
turtle.colormode(255)
color_list = []
colors = colorgram.extract('image.jpg', 25657)
for new_colors in colors:
    rgb = new_colors.rgb
    color_list.append((rgb[0], rgb[1], rgb[2]))

timmy = Turtle()
timmy.speed(0)


def draw_dot():

    x = -360
    y = -300
    timmy.penup()
    timmy.goto(x, y)

    while True:
        if timmy.ycor() > 250:
            timmy.hideturtle()
            break
        random_color = random.choice(color_list)
        timmy.pendown()
        timmy.fillcolor(random_color)
        timmy.begin_fill()

        timmy.circle(20)

        timmy.end_fill()
        timmy.penup()
        timmy.forward(75)

        if timmy.xcor() > 370:

            y = y + 50
            timmy.goto(x, y)


draw_dot()

screen = Screen()
screen.exitonclick()
