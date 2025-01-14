import random
from turtle import Turtle

class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.shape("circle")
        self.penup()
        self.shapesize(0.2, 0.2, 2)
        self.refresh()

    def refresh(self):
        self.goto(random.randint(-250,250),random.randint(-250,250))

