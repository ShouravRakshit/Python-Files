import turtle

from turtle import Turtle, Screen

turtle.colormode(255)
tim = Turtle()
tim.speed("fast")
timmy = Turtle()
timmy.speed(0)

for i in range(100):
    timmy.circle(100)
    timmy.left(5)

screen = Screen()
screen.exitonclick()
