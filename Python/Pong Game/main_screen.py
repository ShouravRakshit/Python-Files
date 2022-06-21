from turtle import Screen
from first_paddle import FirstPaddle
from second_paddle import SecondPaddle
from ball import Ball
from score_board import ScoreBoard
import time

screen = Screen()
# Created a screen with width of 900 and height of 600.

screen.setup(900, 600)
screen.bgcolor("black")
screen.tracer(0)
player_one = FirstPaddle()
player_two = SecondPaddle()
game_ball = Ball((0, 0))
score = ScoreBoard()

# starts listening
screen.listen()
screen.onkey(player_one.move_up, 'Up')
screen.onkey(player_one.move_down, 'Down')
screen.onkey(player_two.move_up, "w")
screen.onkey(player_two.move_down, "s")

game_on = True

while game_on:
    screen.update()
    time.sleep(.09)
    game_ball.move()

    # If it collides with the wall, it will just bounce the ball back.
    if game_ball.pong_ball.ycor() > 280 or game_ball.pong_ball.ycor() < -275:
        game_ball.wall_bounce()

    # If it collides with the second paddle
    elif game_ball.pong_ball.xcor() > 400 and player_two.paddle_one.distance(game_ball.pong_ball) < 45:
        game_ball.paddle_bounce()

    # If it collides with the first paddle
    elif game_ball.pong_ball.xcor() < -400 and player_one.paddle_one.distance(game_ball.pong_ball) < 45:
        game_ball.paddle_bounce()

    # If the x coordinate of the ball is greater than 450, than the first paddle will gain one point.
    elif game_ball.pong_ball.xcor() > 450:
        score.paddle_one_score()
        game_ball.reset_ball()

    # If the x coordinate of the ball is lesser than -450, than the first paddle will gain one point.
    elif game_ball.pong_ball.xcor() < -450:
        score.paddle_two_score()
        game_ball.reset_ball()


screen.exitonclick()
