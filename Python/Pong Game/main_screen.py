from turtle import Screen
from first_paddle import FirstPaddle
from second_paddle import SecondPaddle
from ball import Ball
import time

screen = Screen()
# Created a screen with width of 900 and height of 600.

screen.setup(900, 600)
screen.tracer(0)
player_one = FirstPaddle()
player_two = SecondPaddle()
game_ball = Ball((0, 0))

# starts listening
screen.listen()
screen.onkey(player_one.move_up, 'Up')
screen.onkey(player_one.move_down, 'Down')
screen.onkey(player_two.move_up, "w")
screen.onkey(player_two.move_down, "s")

game_on = True

while game_on:
    screen.update()
    time.sleep(.1)
    game_ball.move()

    # If it collides with the wall, it will just bounce the ball back.
    if game_ball.pong_ball.ycor() > 280 or game_ball.pong_ball.ycor() < -275:
        game_ball.bounce_back()


screen.exitonclick()
