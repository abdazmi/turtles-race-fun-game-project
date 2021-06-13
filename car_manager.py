from turtle import Turtle
from random import Random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]

STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 5


class CarManager:
    def __init__(self):
        self.Cars = []
        self.X = 6

    def create_car(self):
        easy_mode = Random().randint(1, self.X)
        if easy_mode == 1:
            colors = Random().choice(COLORS)
            y = Random().randint(-250, 250)

            new_car = Turtle("square")
            new_car.setheading(180)
            new_car.penup()
            new_car.shapesize(stretch_wid=0.7, stretch_len=2)
            new_car.goto(x=300, y=y)
            new_car.color(colors)
            self.Cars.append(new_car)

    def move_baby(self):
        for car in self.Cars:
            car.forward(STARTING_MOVE_DISTANCE)

    def next_level(self):
        global STARTING_MOVE_DISTANCE, MOVE_INCREMENT
        STARTING_MOVE_DISTANCE += MOVE_INCREMENT
        if self.X > 1:
            self.X -= 1

