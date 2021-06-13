from turtle import Turtle

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 20
FINISH_LINE_Y = 280


class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.setheading(90)
        self.penup()
        self.color("blue")
        self.goto(STARTING_POSITION)

    def run(self):
        self.forward(MOVE_DISTANCE)

    def return_to_starting_point(self):
        self.goto(STARTING_POSITION)