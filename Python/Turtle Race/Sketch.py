from turtle import Turtle, Screen

timmy = Turtle()
timmy.speed(0)


def move_forward():
    timmy.forward(30)


def move_backward():
    timmy.backward(30)


def move_left():
    timmy.left(10)


def move_right():
    timmy.right(10)


def clear():
    timmy.reset()


screen = Screen()
screen.listen()
screen.onkey(key="w", fun=move_forward)
screen.onkey(key="s", fun=move_backward)
screen.onkey(key="a", fun=move_left)
screen.onkey(key="d", fun=move_right)
screen.onkey(key="c", fun=clear)

screen.exitonclick()
