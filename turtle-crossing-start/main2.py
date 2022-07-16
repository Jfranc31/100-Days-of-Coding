import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
tim = Player()
screen.listen()
screen.onkey(fun=tim.move_forward, key="Up")

car_manager = CarManager()
all_cars = car_manager.create_n_cars()

scoreboard = Scoreboard()

game_is_on = True
step = 0
count = 0
car_len = [len(all_cars)]
# print(f"len(all_cars): {len(all_cars)}")
# print(f"car_len: {car_len}")
while game_is_on:
    time.sleep(0.1)
    screen.update()
    step += 1
    # print(len(all_cars))
    if step == 10:
        all_cars.extend(car_manager.create_n_cars())
        car_len.append(len(all_cars))
        # print(f"car_len: {car_len}")
        # print(len(all_cars) - car_len[count])
        # car_len.append()
        step = 0
        count += 1

    if count == 13:
        del all_cars[:car_len[0]]
        del car_len[0]
        count = 0

    for car in all_cars:
        # print(f"type(car): {type(car)}")
        # print(f"car: {car}")
        if tim.distance(car) < 30:
            game_is_on = False
            scoreboard.game_over()
        car.move_cars(scoreboard.num_of_level)

    if tim.finish_line():
        scoreboard.change_score()

screen.exitonclick()
