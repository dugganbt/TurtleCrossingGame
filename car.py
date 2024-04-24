import random
from turtle import Turtle


COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5


class Car(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("square")
        self.penup()
        self.shapesize(1, 2)
        self.color(random.choice(COLORS))
        self.goto(250, random.randint(-240, 240))
        self.setheading(180)
        self.move_car(STARTING_MOVE_DISTANCE)

    def move_car(self, move_increment):
        self.forward(move_increment)
