import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
screen.listen()
timmy = Player()
score = Scoreboard()

screen.onkey(key="Up", fun=timmy.run)
cars = CarManager()

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    cars.create_car()
    cars.move_baby()
    screen.update()

    for car in cars.Cars:
        if timmy.distance(car) < 20:
            game_is_on = False
            score.game_over()

    if timmy.ycor() > 300:
        timmy.return_to_starting_point()
        score.refresh()
        time.sleep(1)
        cars.next_level()


screen.exitonclick()