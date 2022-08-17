from turtle import Turtle

STARTINH_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.shape('turtle')
        self.color('black')
        self.got_to_start()
        self.setheading(90)

    def go_up(self):
        self.forward(MOVE_DISTANCE)

    def got_to_start(self):
        self.goto(STARTINH_POSITION)

    def is_at_finish_line(self):
        return self.ycor() > 280
