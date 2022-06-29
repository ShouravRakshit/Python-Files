from turtle import *

import turtle

ws = turtle.Screen()
ws.setup(400, 300)
place_holder = turtle.textinput("Python Guides", "Enter your Name")
turtle.penup()
turtle.hideturtle()
turtle.goto(10, 20)
turtle.write(place_holder)
ws.exitonclick()