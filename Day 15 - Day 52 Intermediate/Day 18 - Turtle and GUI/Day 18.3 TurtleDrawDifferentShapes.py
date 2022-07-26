from turtle import Turtle, Screen
from random import choice


raphael = Turtle()
raphael.shape("turtle")
raphael.color('red')


def random_pen_color():
    color_set = ['0', '1', '2', '3', '4', '5', '6',
                 '7', '8', '9', 'a', 'b', 'c', 'd', 'e', 'f']
    color = "#"
    for _ in range(6):
        color += choice(color_set)
    return color


def shape(sides):
    raphael.pencolor(random_pen_color())
    angle = 360/sides
    for _ in range(sides):
        raphael.forward(100)
        raphael.right(angle)


for _ in range(3, 11):
    shape(_)

screen = Screen()
screen.exitonclick()
