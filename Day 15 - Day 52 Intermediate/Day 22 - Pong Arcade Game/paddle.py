from turtle import Turtle


class Paddle(Turtle):

    def __init__(self):
        super().__init__()
        self.shape('square')
        self.color('white')
        self.width(20)
        self.height(100)
        self.xcor(350)
        self.ycor(0)