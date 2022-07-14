import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

player = Player()
car_manager = CarManager()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(fun=player.move_forward, key="Up")

game_is_on = True

while game_is_on:
    time.sleep(0.1)
    screen.update()

    if player.finish_line():
        scoreboard.change_score()

    car_manager.create_car()

    for car in car_manager.all_cars:
        if player.distance(car) < 30:
            game_is_on = False
            scoreboard.game_over()

    car_manager.move_cars(scoreboard.num_of_level)

screen.exitonclick()
