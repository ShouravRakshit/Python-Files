from first_paddle import FirstPaddle

X = 430


# This class inherits everything from first_paddle.
class SecondPaddle(FirstPaddle):

    def __init__(self):
        super().__init__()

        self.paddle_one.goto(X, self.y)

    def move_up(self):
        self.y = self.y + 50
        self.paddle_one.goto(X, self.y)

    def move_down(self):
        self.y = self.y - 50
        self.paddle_one.goto(X, self.y)
