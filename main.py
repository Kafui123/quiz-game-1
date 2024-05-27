from turtle import Screen
import time  # imported the time module for to control the screen.update function
from giraffe import Giraffe
from food import Food
from scoreboard import Scoreboard


UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My amazing game")

screen.tracer(0)
bob = Giraffe()
food = Food()
scoreboard = Scoreboard()

screen.listen()  # This code is used for listening to keyboard inputs
screen.onkey(bob.up, "Up")
screen.onkey(bob.down, "Down")
screen.onkey(bob.left, "Left")
screen.onkey(bob.right, "Right")


game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)


    bob.move()

    # Detect the collision with the food
    if bob.head.distance(food) < 12:
        food.refresh()
        bob.extend()
        scoreboard.increase_score()


    # Detect collision with wall
    if bob.head.xcor() > 280 or bob.head.xcor() < -280 or bob.head.ycor() > 280 or bob.head.ycor() < -280:
        game_is_on = False
        scoreboard.game_over()

    # Detect collision with tail
    for segment in bob.segments[1:]:
        if bob.head.distance(segment) < 10:
            game_is_on = False
            scoreboard.game_over()







screen.exitonclick()
