from turtle import Turtle, Screen

square = Turtle()
for i in range(4):
    square.forward(50)
    square.left(90)

screen = Screen()
screen.exitonclick()

