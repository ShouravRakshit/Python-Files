from turtle import Turtle, Screen, textinput
import pandas
turtle = Turtle()
screen = Screen()
tim = Turtle()
screen.addshape("blank_states_img.gif")
turtle.shape("blank_states_img.gif")
tim.penup()
tim.hideturtle()
data = pandas.read_csv("50_states.csv")
# Creating list for the state names.
states_list = data["state"].to_list()
# Creating x coordinate list for the states.
x_coordinate = data["x"].to_list()
# Creating y coordinate list for the states.
y_coordinate = data["y"].to_list()
correct_answer = 0
quiz_on = True
while quiz_on:
    user_input = textinput(f"{correct_answer}/ 50 States Correct", "Guess a another state")

    for state_name in range(len(states_list)):
        # Checking if the state name is correct.
        if user_input == states_list[state_name].lower():
            tim.goto(x_coordinate[state_name], y_coordinate[state_name])
            tim.write(states_list[state_name])
            correct_answer += 1
        # To exit the program type exit.
        elif user_input == "exit":
            quiz_on = False
