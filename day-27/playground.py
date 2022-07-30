def add(*args):
    total = 0
    for num in args:
        total += num
    return total


print(add(1, 2, 3, 4))


def calculate(n, **kwargs):
    print(kwargs)
    # for key, value in kwargs.items():
    #     print(key)
    #     print(value)
    n += kwargs["add"]
    n *= kwargs["multiply"]
    print(n)


calculate(2, add=3, multiply=5)


class Car:
    def __init__(self, **kwargs):
        self.make = kwargs.get("make")
        self.model = kwargs.get("model")
        self.color = kwargs.get("color")
        self.seats = kwargs.get("seats")


my_car = Car(make="Nissan", model="GT-R", color="black", seats="5")
print(my_car.make + " " + my_car.model + " " + my_car.color + " " + my_car.seats)
