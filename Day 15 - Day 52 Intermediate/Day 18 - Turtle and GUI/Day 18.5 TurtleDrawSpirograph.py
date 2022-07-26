import turtle
import random

tim = turtle.Turtle()
tim.speed(0)


def spirograph():
    for _ in range(72):
        tim.color(
            f"#{''.join(random.choices(['0', '1', '2', '3', '4', '5', '6','7', '8', '9', 'a', 'b', 'c', 'd', 'e', 'f'],k=6))}")
        tim.circle(100)
        tim.right(5)


spirograph()

screen = turtle.Screen()
screen.exitonclick()
