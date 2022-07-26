import turtle
import random

michael_angelo = turtle.Turtle()
michael_angelo.pensize(5)
michael_angelo.speed(0)


def walk():
    michael_angelo.right(random.choice([0, 90, 180, 270]))
    michael_angelo.pencolor(
        f"#{''.join(random.choices(['0', '1', '2', '3', '4', '5', '6','7', '8', '9', 'a', 'b', 'c', 'd', 'e', 'f'],k=6))}")
    michael_angelo.forward(10)


for _ in range(1000):
    walk()

screen = turtle.Screen()
screen.exitonclick()
