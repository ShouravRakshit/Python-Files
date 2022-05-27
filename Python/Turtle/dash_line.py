from turtle import Turtle, Screen

tim = Turtle()
for i in range(10):
    tim.up()
    tim.forward(10)
    tim.down()
    tim.forward(10)


screen = Screen()
screen.exitonclick()