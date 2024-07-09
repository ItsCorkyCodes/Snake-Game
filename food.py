from random import randrange
from turtle import Turtle


class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.speed('fastest')
        self.color("red")
        self.shape("circle")
        self.shapesize(0.5, 0.5)
        self.refresh()

    def refresh(self):
        new_x = randrange(-260, 260, 20)
        new_y = randrange(-260, 260, 20)
        self.goto(new_x, new_y)
