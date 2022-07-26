from turtle import Turtle, Screen

donatello = Turtle()
donatello.shape("turtle")
donatello.color("purple")

for i in range(4):
    donatello.forward(100)
    donatello.right(90)

screen = Screen()

screen.exitonclick()
