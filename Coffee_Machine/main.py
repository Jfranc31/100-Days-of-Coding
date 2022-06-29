from flavors import MENU, resources

profit = 0


def cash():
    """ Returns total amount from customer """
    print("Please insert coins.")
    quarters = int(input("how many quarters?: "))
    dimes = int(input("how many dimes?: "))
    nickles = int(input("how many nickles?: "))
    pennies = int(input("how many pennies?: "))
    total = format(quarters * 0.25 + dimes * 0.1 + nickles * 0.05 + pennies * 0.01, '.2f')
    return total


def transaction(money, coffee):
    """ Adds money to profit, reduces ingredients, gives change to customer """
    global profit
    resources['water'] -= MENU[coffee]['ingredients']['water']
    if 'milk' in MENU[coffee]['ingredients']:
        resources['milk'] -= MENU[coffee]['ingredients']['milk']
    resources['coffee'] -= MENU[coffee]['ingredients']['coffee']
    if float(money) > MENU[coffee]['cost']:
        change = round(float(money) - MENU[coffee]['cost'], 2)
        profit += MENU[coffee]['cost']
        print(f"Here is ${change} dollars in change.")
        print(f"Here is your {coffee} ☕️. Enjoy!")
    else:
        print(f"Here is your {coffee} ☕️. Enjoy!")
        profit += MENU[coffee]['cost']


def check_resources(coffee):
    """ Verifies if we have resources """
    if resources['water'] >= MENU[coffee]['ingredients']['water']:
        if resources['coffee'] >= MENU[coffee]['ingredients']['coffee']:
            if 'milk' in MENU[coffee]['ingredients']:
                if resources['milk'] >= MENU[coffee]['ingredients']['milk']:
                    customer_cash = cash()
                    if float(customer_cash) >= MENU[coffee]['cost']:
                        transaction(customer_cash, choice)
                    else:
                        print("Sorry that's not enough money. Money refunded.")
            elif 'milk' not in MENU[coffee]['ingredients']:
                customer_cash = cash()
                if float(customer_cash) >= MENU[coffee]['cost']:
                    transaction(customer_cash, choice)
                else:
                    print("Sorry that's not enough money. Money refunded.")
            else:
                print("Not enough milk. Money refunded.")
        else:
            print("Not enough coffee. Money refunded.")
    else:
        print("Not enough water. Money refunded.")


is_open = True

while is_open:
    choice = input("What would you like? (espresso/latte/cappuccino): ").lower()
    if choice == 'off':
        is_open = False
    elif choice == 'report':
        print(f"Water: {resources['water']}ml\nMilk: {resources['milk']}ml\nCoffee: {resources['coffee']}g")
        print(f"Money: ${profit}")
    elif choice == 'espresso' or choice == 'latte' or choice == 'cappuccino':
        check_resources(choice)
    else:
        print("Invalid option. Try again.")
