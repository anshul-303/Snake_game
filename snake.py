import time
from turtle import Screen, Turtle
import sys
import random
import turtle

MOVE_DISTANCE=20

class Snake:
    def __init__(self):
        self.turts = []
        self.create_snake()
        self.head=self.turts[0]
        self.n=len(self.turts)

    def create_snake(self):
        for i in range(0, 3):
              new_turtle = Turtle("square")
              self.turts.append(new_turtle)
              self.turts[i].color("white")
              self.turts[i].penup()
              self.turts[i].speed(1)
              self.turts[i].goto(-i * MOVE_DISTANCE, 0)

    def add_segment(self, position):
        new_turtle = Turtle("square")
        new_turtle.penup()
        new_turtle.color("white")
        new_turtle.speed(1)
        new_turtle.goto(position)
        self.turts.append(new_turtle)

    def move(self):
        for i in range(len(self.turts) - 1, 0, -1):
            new_x = self.turts[i - 1].xcor()
            new_y = self.turts[i - 1].ycor()
            self.turts[i].goto(new_x, new_y)
        self.head.forward(MOVE_DISTANCE)

    def extend(self):
        self.add_segment(self.turts[-1].position())

    def turn_right(self):
        if self.head.heading() != 180:  # Prevent reversing direction
           self.turts[0].setheading(0)
    def turn_left(self):
        if self.head.heading() != 0:  # Prevent reversing direction
           self.turts[0].setheading(180)
    def turn_up(self):
        if self.head.heading() != 270:  # Prevent reversing direction
           self.turts[0].setheading(90)
    def turn_down(self):
        if self.head.heading() != 90 :
           self.turts[0].setheading(270)


