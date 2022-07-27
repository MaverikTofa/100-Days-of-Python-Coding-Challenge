from turtle import Turtle, Screen

tim = Turtle()
screen = Screen()


def w_forward():
    tim.forward(10)


def s_backward():
    tim.backward(10)


def a_counter_clockwise():
    tim.left(5)


def d_clockwise():
    tim.right(5)


def clear():
    tim.reset()


screen.listen()
screen.onkey(w_forward, "w")
screen.onkey(s_backward, "s")
screen.onkey(a_counter_clockwise, "a")
screen.onkey(d_clockwise, "d")
screen.onkey(clear, "c")

screen.exitonclick()
