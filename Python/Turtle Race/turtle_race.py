from turtle import Turtle, Screen
import random

colors = ["red", "orange", "yellow", "green", "blue", "purple"]
screen = Screen()
user_text = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter a color: ")

screen.setup(width=500, height=500)
x = -240
y = -200
turtels = []

for ninja in range(6):
    # Creating six turtle objects.
    timon = Turtle("turtle")
    turtels.append(timon)
    timon.penup()
    timon.color(colors[ninja])
    timon.goto(x, y)
    y = y + 80


condition = True
while condition:
    for ninja in range(len(turtels)):
        turtels[ninja].forward(random.randint(1, 10))
        # Using the forward method so that all the turtle moves forward.
        if turtels[ninja].xcor() > 230:
            # The first turtle that reaches the end first will win the race.
            if user_text == colors[ninja]:
                # This will check which turtle won the race.
                print(f"You won {colors[ninja]}")

            else:
                print(f"You lost the bet, The winner is {colors[ninja]}")
            condition = False


screen.exitonclick()
