from turtle import Screen
from snake import Snake
import time
from screen_board import Score
from food import Food


screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("The Snake Game")
screen.tracer(0)
snake = Snake()
food = Food()
score_board = Score()

screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

screen.listen()

condition = True
while condition:
    screen.update()
    time.sleep(.1)
    snake.move()

    # When the snake head collides with the food.
    if snake.snake_head.distance(food.meal) < 18:
        food.new_food_location()
        score_board.increase_score()
        snake.extend_body()

    # When it hits the boundary of the game.
    if snake.snake_head.xcor() >= 290 or snake.snake_head.xcor() <= -290 or snake.snake_head.ycor() >= 250 or \
            snake.snake_head.ycor() <= -290:
        score_board.game_over()
        condition = False


screen.exitonclick()

