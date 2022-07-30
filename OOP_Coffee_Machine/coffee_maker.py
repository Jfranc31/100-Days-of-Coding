from extra_functions import resource_number


class CoffeeMaker:
    """
    Models the machine that makes the coffee and the value each resource has.
    """
    def __init__(self):
        self.resources = {
            "water": 1000,
            "milk": 1000,
            "coffee": 300,
        }

    def report(self):
        """
        Prints a report of all resources and the value it has.
        """
        print(f"Water: {self.resources['water']}ml")
        print(f"Milk: {self.resources['milk']}ml")
        print(f"Coffee: {self.resources['coffee']}g")

    def is_resource_sufficient(self, drink):
        """
        Returns True when order can be made, False if ingredients are insufficient.

            parameters:
                drink (string): name of the drink
            returns:
                can_make (Boolean): True or False
        """
        can_make = True
        for item in drink.ingredients:
            if drink.ingredients[item] > self.resources[item]:
                can_make = False
        return can_make

    def make_coffee(self, order):
        """
        Deducts the required ingredients from the resources.

            parameters:
                order (string): name of drink
        """
        for item in order.ingredients:
            self.resources[item] -= order.ingredients[item]
        print(f"Here is your {order.name} ☕️. Enjoy!")

    def refill(self):
        """
        Adds a value user inputs to the resource they would like to increase.
        """
        choose = True
        pick = 0
        while choose:
            self.report()
            pick = input("Which resource would you like to refill? (1: water, 2: milk, 3: coffee): ")
            if pick in ['1', '2', '3', 'water', 'milk', 'coffee']:
                choose = False
            else:
                print("Not an option, try again.")
        how_much = int(input("How much would you want to refill it by? "))
        if pick.isnumeric():
            item = resource_number(int(pick))
        else:
            item = pick
        self.resources[item] += how_much
