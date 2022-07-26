from turtle import Turtle, Screen, width

leonardo = Turtle()
leonardo.shape('turtle')
leonardo.color('blue')

leonardo.hideturtle()
leonardo.up()
leonardo.setposition(-200, 50)
leonardo.showturtle()

for _ in range(50):
    leonardo.forward(5)
    leonardo.up()
    leonardo.forward(3)
    leonardo.down()

screen = Screen()

screen.exitonclick()
