from turtle import Turtle

UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake:

    def __init__(self):
        # initial position of the snake.
        self.x = -20
        self.y = 0
        self.snake_segments = []
        self.creating_snake_body()
        self.snake_head = self.snake_segments[0]

    # Creating the body of the snake by creating three objects using for loop.
    def creating_snake_body(self):
        for i in range(3):
            snake = Turtle("square")
            snake.penup()
            self.snake_segments.append(snake)
            snake.color("white")
            snake.goto(self.x, self.y)
            # Changing only the x coordinate by 20 because every square is by default 20px.
            self.x = self.x + 20

    # Extend the body of the snake when it eats food.
    def extend_body(self):
        snake = Turtle("square")
        snake.speed(0)
        snake.penup()
        self.snake_segments.append(snake)
        snake.color("white")
        snake.goto(self.snake_segments[-1].pos())

    # Moving the Snake body.
    def move(self):
        for segment in range(len(self.snake_segments) - 1, 0, -1):
            # Changing the position of the snake body other than the first one. Other body parts will change its
            # position. For example, the second square of the body part will go to the position of the first square of
            # the body part and third will go to the position of the second one and so forth.
            new_x = self.snake_segments[segment - 1].xcor()
            new_y = self.snake_segments[segment - 1].ycor()
            self.snake_segments[segment].goto(new_x, new_y)
        self.snake_head.forward(20)

    def up(self):
        if self.snake_head.heading() != DOWN:
            self.snake_head.seth(UP)

    def down(self):
        if self.snake_head.heading() != UP:
            self.snake_head.seth(DOWN)

    def left(self):
        if self.snake_head.heading() != RIGHT:
            self.snake_head.seth(LEFT)

    def right(self):
        if self.snake_head.heading() != LEFT:
            self.snake_head.seth(RIGHT)
