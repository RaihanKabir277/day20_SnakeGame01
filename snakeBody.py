
from turtle import Turtle, Screen
# import random
import time
from snake import Snake


screen = Screen()
screen.setup(600, 600)
screen.bgcolor("black")
screen.title("Snake Game ~")
screen.tracer(0)

snake = Snake()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

# cordinate_list = [0, -20, -40]
# segments = []

# for i in range(3):
#     timmy = Turtle("square")
#     timmy.color("white")
#     timmy.goto(cordinate_list[i], 0)
#     segments.append(timmy)

# --------- another way for do this ---------
# coordinate_list = [(0, 0), (-20, 0), (-40, 0)]
# segments = []      #oop added that is why we transfer this into snake class

game_is_on = True


# for position in coordinate_list:
#     timmy = Turtle("square")
#     timmy.color("white")         #this portion of code wil find in snake class
#     timmy.penup()
#     timmy.goto(position)
#     segments.append(timmy)

while game_is_on:
    screen.update()
    time.sleep(0.2)
    # for i in segments:
    #     # screen.update()
    #     i.forward(20)
    #     # time.sleep(1)   #there will arise a problem , if we want to move its by left right position

    # for seg in range(len(segments) - 1 , 0, -1):
    #     new_x = segments[seg - 1].xcor()
    #     new_y = segments[seg - 1].ycor()
    #     segments[seg].goto(new_x, new_y)
    
    # segments[0].forward(20)
    # segments[0].left(90)

# --------------- convert this into class method ----------

    snake.move()


screen.exitonclick()

