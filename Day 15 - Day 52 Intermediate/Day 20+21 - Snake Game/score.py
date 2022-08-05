from ctypes import alignment
from turtle import Turtle


class Score(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.color('white')
        self.hideturtle()
        self.write(f"Score: {self.score}", align='center')
