
from turtle import Screen
import time
from snake import Snake
from food import Food


screen = Screen()
screen.setup(600, 600)
screen.bgcolor("black")
screen.title("Snake Game ~")
screen.tracer(0)

snake = Snake()
food = Food()


screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")



game_is_on = True



while game_is_on:
    screen.update()
    time.sleep(0.2)
    

    snake.move()


screen.exitonclick()

