import random
from turtle import Turtle


class Food:

    def __init__(self):
        self.meal = Turtle("circle")
        self.meal.penup()
        self.meal.color("red")
        self.meal.speed(0)
        self.new_food_location()

    def new_food_location(self):
        x_location = random.randint(-280, 280)
        y_location = random.randint(-250, 240)
        self.meal.goto(x_location, y_location)
