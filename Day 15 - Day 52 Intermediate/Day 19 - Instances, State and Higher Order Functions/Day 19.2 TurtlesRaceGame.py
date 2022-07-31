from turtle import Turtle, Screen
from random import randint
import turtle

screen = Screen()
screen.setup(500, 400)
user_bet = screen.textinput(title="Make your ber",
                            prompt="Which turtle will win the race? Enter a color: ")

colors_position = [{"color": "red", "position": -70}, {"color": "orange", "position": -40},
                   {"color": "yellow", "position": -
                       10}, {"color": "green", "position": 20},
                   {"color": "blue", "position": 50}, {"color": "purple", "position": 80}]

all_turtles = []
for _ in colors_position:
    tim = Turtle('turtle')
    tim.up()
    tim.color(_["color"])
    tim.goto(x=-230, y=_["position"])
    all_turtles.append(tim)

is_race_on = False
if user_bet:
    is_race_on = True

while is_race_on:
    for turtle in all_turtles:
        if turtle.xcor() > 230:
            is_race_on = False
            winning = turtle.pencolor()
            if winning == user_bet:
                print(f"You've won!, The {winning} turtle won the race!")
            else:
                print(f"You've lost! The {winning} turtle won the race!")
        random_distance = randint(0, 10)
        turtle.forward(random_distance)


screen.exitonclick()
