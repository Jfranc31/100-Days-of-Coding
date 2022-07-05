# TODO - Docstrings
# TODO - Raise exception for wrong inputs
# TODO - How much money each is worth
# TODO - Create unit tests
# TODO - Fix presentation
class MenuItem:
    """
    Models each drink with the name, amount of water, milk and coffee it takes to make and the cost of the drink.
    """
    def __init__(self, name, water, milk, coffee, cost):
        self.name = name
        self.cost = cost
        self.ingredients = {
            "water": water,
            "milk": milk,
            "coffee": coffee
        }


class Menu:
    """
    Models the Menu with drinks and their requirements.
    """
    def __init__(self):
        self.menu = [
            MenuItem(name="latte", water=200, milk=150, coffee=24, cost=2.5),
            MenuItem(name="espresso", water=50, milk=0, coffee=18, cost=1.5),
            MenuItem(name="cappuccino", water=250, milk=50, coffee=24, cost=3),
        ]

    def get_items(self):
        """
        Returns all the names of the available menu items
            returns:
                options (list): each drink on the menu
        """
        options = []
        for item in self.menu:
            options.append(item.name)
        return options

    def find_drink(self, order_name):
        """
        Searches the menu for a particular drink by name. Returns that item if it exists, otherwise returns None
            returns:
                item (string): name of drink
        """
        for item in self.menu:
            if item.name == order_name:
                return item
        # print("Sorry that item is not available.")

    def drink_number(self, number: int):
        """
        Sets a number to the drink so user can input number instead of writing out the drink.
            returns:
                drinks.get (dict): dictionary with name of drink to a number
        """
        count = 0
        drinks = {}
        for drink in self.menu:
            count += 1
            drinks[count] = drink.name
        return drinks.get(number, 'Wrong number: 1-3')
