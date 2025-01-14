import sys
import time
from turtle import Turtle
from turtle import Screen
from snake import Snake
from food import Food


my_screen = Screen()
BOUNDARY_WIDTH=600
BOUNDARY_HEIGHT=600
my_screen.setup(BOUNDARY_WIDTH, BOUNDARY_HEIGHT)
BOUNDARY = BOUNDARY_WIDTH // 2 - 20
my_screen.colormode(255)
my_screen.bgcolor("black")
my_screen.title("Snake Game")
my_screen.tracer(0)

snake=Snake()
my_screen.listen()
food=Food()

name_writer = Turtle()
name_writer.hideturtle()  # Hide the turtle cursor
name_writer.penup()       # Lift the pen to avoid drawing
name_writer.color("white")  # Set text color
name_writer.goto(0, 250)  # Centered horizontally, near the top
start_score=0
name_writer.write(f"Score : {start_score} ", align="center", font=("Arial", 24, "bold"))
game_is_on = True

gameover=Turtle()
gameover.hideturtle()  # Hide the turtle cursor
gameover.penup()       # Lift the pen to avoid drawing
gameover.color("white")  # Set text color
gameover.goto(0, 0)
# Centered horizontally, near the top

while game_is_on:
    my_screen.update()
    time.sleep(0.1)
    snake.move()

    my_screen.onkey(fun=snake.turn_right, key="Right")
    my_screen.onkey(fun=snake.turn_left, key="Left")
    my_screen.onkey(fun=snake.turn_up, key="Up")
    my_screen.onkey(fun=snake.turn_down, key="Down")

    if snake.head.distance(food) < 15:
        food.refresh()
        start_score+=1
        name_writer.clear()
        name_writer.write(f"Score : {start_score}", align="center", font=("Arial", 24, "bold"))
        snake.extend()

    if (
            snake.head.xcor() > BOUNDARY or snake.head.xcor() < -BOUNDARY or
            snake.head.ycor() > BOUNDARY or snake.head.ycor() < -BOUNDARY
    ):
        game_is_on = False
        gameover.write("Game Over.", align="center", font=("Arial", 24, "bold"))

    for turt in snake.turts[1:]:

        if snake.head.distance(turt) < 15:
            game_is_on = False
            gameover.write("Game Over.", align="center", font=("Arial", 24, "bold"))

    else:
        pass
my_screen.exitonclick()
