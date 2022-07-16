from turtle import Turtle
import random
COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 5

# for main2


# class CarManager(Turtle):
#     def __init__(self, ):
#         super().__init__()
#
#     def create_car(self):
#         """create random cars that go left """
#         self.shape("square")
#         self.penup()
#         self.shapesize(stretch_wid=1, stretch_len=2)
#         self.color(random.choice(COLORS))
#         self.goto(random.randint(250, 290), random.randint(-250, 260))
#
#     @classmethod
#     def initiate_n_cars(cls, *n_car):
#         return [CarManager() for _ in n_car]
#
#     def create_n_cars(self):
#         n_car = list(range(random.randint(1, 5)))
#         cars = self.initiate_n_cars(*n_car)
#         for car in cars:
#             car.create_car()
#         return cars
#
#     def move_cars(self, speed):
#         add = (speed - 1) * MOVE_INCREMENT
#         self.backward(STARTING_MOVE_DISTANCE + add)


# for main


class CarManager:
    def __init__(self):
        """
        Initialize empty list for all the cars.
        """
        self.all_cars = []

    def create_car(self):
        """
        Make a car only everytime the dice rolls a one and add to list of cars.
        """
        random_chance = random.randint(1, 6)
        if random_chance == 1:
            new_car = Turtle("square")
            new_car.penup()
            new_car.shapesize(stretch_wid=1, stretch_len=2)
            new_car.color(random.choice(COLORS))
            new_car.goto(300, random.randint(-250, 250))
            self.all_cars.append(new_car)

    def move_cars(self, speed):
        """
        Car moves a certain distance depending on the level the game is on, increasing as level increases by the
        MOVE_INCREMENT.
            parameter speed: The level that the player is at.
        """
        for car in self.all_cars:
            add = (speed - 1) * MOVE_INCREMENT
            car.backward(STARTING_MOVE_DISTANCE + add)
