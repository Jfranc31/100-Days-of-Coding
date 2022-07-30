from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine
from extra_functions import add_drink

if __name__ == '__main__':
    coffee_maker = CoffeeMaker()
    money_machine = MoneyMachine()
    menu = Menu()

    is_on = True

    while is_on:
        items = menu.get_items()
        options = '\n'
        count = 0
        for item in items:
            drink = menu.find_drink(item)
            if coffee_maker.is_resource_sufficient(drink):
                count += 1
                options += f"{count}: " + item + " $" + str("%.2f" % round(drink.cost, 2)) + " \n"
            else:
                count += 1

        choice = input(f"What would you like? {options} ")
        opt = range(len(items) + 1)
        if choice == 'off':
            is_on = False
        elif choice == 'report':
            coffee_maker.report()
            money_machine.report()
        elif choice == 'refill':
            coffee_maker.refill()
        elif choice == 'add':
            new_drink = add_drink()
            test = MenuItem(new_drink[0], new_drink[1], new_drink[2], new_drink[3], new_drink[4])
            menu.menu.append(test)
        elif (choice in items) or (choice.isnumeric() in opt):
            if choice.isnumeric():
                drink_choice = menu.drink_number(int(choice))
            else:
                drink_choice = choice
            drink = menu.find_drink(drink_choice)
            if drink is None:
                print("Not an option, try again.")
            else:
                if coffee_maker.is_resource_sufficient(drink):
                    if money_machine.make_payment(drink.cost):
                        coffee_maker.make_coffee(drink)
                    else:
                        print("Not an option, try again.")
                else:
                    print("Not enough resources to make at the moment, try again.")
        else:
            print("Not an option, try again.")

# TODO - credit card incurs fee
# TODO - don't pick drink, tell wrong, run again
# TODO - handle exception
# TODO - if material isn't there for the drink, dont show option
# TODO - function to add more material, call it refill
