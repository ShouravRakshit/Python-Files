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
difficult_level = .10
# The game is played ten rounds. The one who wins the most rounds will win the game.
# The pace of the ball increases after every round.
while game_on:
    screen.update()
    if difficult_level < .01:
        if score.player_one_score > score.player_two_score:
            print(f"The winner is player one with {score.player_one_score} points")
            game_on = False
        elif score.player_two_score > score.player_one_score:
            print(f"The winner is player two with {score.player_two_score} points")
            game_on = False
        else:
            print("The game is draw")
            game_on = False
    time.sleep(difficult_level)

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
        difficult_level = difficult_level - .01

    # If the x coordinate of the ball is lesser than -450, than the first paddle will gain one point.
    elif game_ball.pong_ball.xcor() < -450:
        score.paddle_two_score()
        game_ball.reset_ball()
        difficult_level = difficult_level - .01

screen.exitonclick()
