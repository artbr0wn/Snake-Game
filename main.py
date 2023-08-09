from turtle import Screen
import time
from snake import Snake
from food import Food
from scoreboard import Scoreboard


# Setting up the GUI
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Art's Snake Game")

#turning off the tracer so that the screen's animation stops when animating each individual turtle block moving
screen.tracer(n=0)
snake = Snake()
food = Food()
user_score = Scoreboard()

game_is_on = True


# Directional movement for the snake
screen.onkey(fun=snake.up, key='w')
screen.onkey(fun=snake.down, key='s')
screen.onkey(fun=snake.left, key='a')
screen.onkey(fun=snake.right, key='d')


while game_is_on:
    screen.update()
    time.sleep(0.1) #ensures that the segments move all as one w/ little delay
    snake.move()
    screen.listen()

    #Detect collision of food with turtle using .distance module in turtle
    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        user_score.score_increase()

    #Detect collision with wall.
    if snake.head.xcor() > 300 or snake.head.xcor() < -300 or snake.head.ycor() > 290 or snake.head.ycor() < -290:
        user_score.reset()
        snake.reset()

    #Detect collision with tail
    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:
            user_score.reset()
            snake.reset()
    # if head collides with any segment in the tail, trigger game over


screen.exitonclick()