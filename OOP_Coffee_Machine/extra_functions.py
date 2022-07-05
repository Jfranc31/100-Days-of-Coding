def resource_number(number: int):
    """
    To keep track of resource user wants based on number value they input.
        returns:
            resources.get (string): name of resource
    """
    resources = {
        1: "water",
        2: "milk",
        3: "coffee"
    }
    return resources.get(number, 'Wrong number: 1-3')


def add_drink():
    """
    User can add a new drink with each requirement needed, name of drink, amount of water, milk, and coffee
    and the cost of the drink.
        returns:
            drink (list): list of requirements user inputted
    """
    name = input("name of drink: ").lower()
    water = int(input("Amount of water to make: "))
    milk = int(input("Amount of milk to make: "))
    coffee = int(input("Amount of coffee to make: "))
    cost = float(input("Amount it costs: "))
    drink = [name, water, milk, coffee, cost]
    return drink
