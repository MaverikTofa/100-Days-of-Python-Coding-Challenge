import turtle
import random


tim = turtle.Turtle()
tim.speed(0)
tim.up()
tim.setposition(-200, -200)
x = -200


def draw_10_dots():
    for _ in range(10):
        tim.fillcolor(
            f"#{''.join(random.choices(['0', '1', '2', '3', '4', '5', '6','7', '8', '9', 'a', 'b', 'c', 'd', 'e', 'f'],k=6))}")
        tim.begin_fill()
        tim.circle(10)
        tim.forward(50)
        tim.end_fill()


for _ in range(10):
    draw_10_dots()
    x += 50
    tim.setposition(-200, x)

screen = turtle.Screen()
screen.exitonclick()
