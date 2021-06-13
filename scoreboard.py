from turtle import Turtle
FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.penup()
        self.hideturtle()
        self.color("red")
        self.goto(y= 250, x= -150)
        self.write(f"Score is: {self.score}", align="center", font= FONT)


    def refresh(self):
        self.clear()
        self.score += 1
        self.write(f"Score is: {self.score}", align="center", font= FONT)

    def game_over(self):
        self.goto(y= 0, x= -50)

        self.write("Game Over", align="center", font= FONT)

