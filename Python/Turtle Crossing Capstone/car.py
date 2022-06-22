import random
import turtle

from turtle import Turtle

turtle.colormode(255)


class Car:

    def __init__(self):
        self.cars_list = []

    # Generating the random color for the cars.
    def random_color(self):
        r = random.randint(0, 255)
        g = random.randint(0, 255)
        b = random.randint(0, 255)
        self.color = (r, g, b)
        return self.color

    # Creating the car object.
    def creating_car(self):
        self.cars = Turtle("square")
        self.cars.color(self.random_color())
        self.cars.shapesize(stretch_wid=.5, stretch_len=1)
        self.cars.setheading(180)
        self.cars.penup()
        self.cars.goto(280, random.randint(-240, 240))
        self.cars_list.append(self.cars)

    def move_forward(self, speed_up):
        for tesla in self.cars_list:
            tesla.forward(speed_up)
