
from turtle import Turtle, Screen
import random


screen = Screen()
screen.setup(600, 600)
screen.bgcolor("black")
screen.title("Snake Game ~")

# cordinate_list = [0, -20, -40]

# for i in range(3):
#     timmy = Turtle("square")
#     timmy.color("white")
#     timmy.goto(cordinate_list[i], 0)

# --------- another way for do this ---------
coordinate_list = [(0, 0), (-20, 0), (-40, 0)]
for position in coordinate_list:
    timmy = Turtle("square")
    timmy.color("white")
    timmy.goto(position)


screen.exitonclick()

