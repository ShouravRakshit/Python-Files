from turtle import Screen
import random
from car import Car
import time
from level import Level
from player import Player


screen = Screen()
screen.tracer(0)
# starts listening
screen.listen()
amount_of_cars = random.randint(10, 20)

user = Player()
vehicles = Car()
level_change = Level()

screen.onkey(user.move_up, 'Up')
screen.onkey(user.move_left, 'Left')
screen.onkey(user.move_right, 'Right')
screen.onkey(user.move_down, "Down")

# Created a screen with a width of 600px and height of 600px
screen.setup(width=600, height=600)

car_on = True
speed_up = 5
while car_on:
    screen.update()
    vehicles.creating_car()
    time.sleep(.1)
    vehicles.move_forward(speed_up)
    # This for loop is going to go through all the cars in the cars_list and check whether any of the car's distance and
    # the turtle distance is less than 20. If the distance is less than 20 then it will stop the game.
    for objects in range(len(vehicles.cars_list)):
        if vehicles.cars_list[objects].distance(user.player) < 20:
            car_on = False

        # If it collides with the wall, then the players level will go up by one and the player will start from the
        # beginning. After each round, the speed of the car will increase by 5.
        if user.player.ycor() > 300:
            level_change.level_up()
            speed_up += 5
            user.reset()

screen.exitonclick()