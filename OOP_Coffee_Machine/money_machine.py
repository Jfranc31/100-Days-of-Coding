class MoneyMachine:

    CURRENCY = "$"

    DOLLAR_VALUES = {
        "10": 10.00,
        "5": 5.00,
        "1": 1.00
    }

    def __init__(self):
        self.profit = 0
        self.card_company_payment = 0
        self.money_received = 0

    def report(self):
        """
        Prints the current profit report.
        """
        print(f"Money: {self.CURRENCY}{self.profit}")
        print(f"Card Company Payment: {self.CURRENCY}{self.card_company_payment}")

    def process_cash(self):
        """
        Returns the total calculated from dollars inserted.
            returns:
                self.money_received (int): Amount of money user inputted in total
        """
        print("Please insert dollars.")
        for dollar in self.DOLLAR_VALUES:
            self.money_received += int(input(f"How many {dollar}?: ")) * self.DOLLAR_VALUES[dollar]
        return self.money_received

    def make_payment(self, cost):
        """
        Returns True when payment is accepted, or False if insufficient.
            parameters:
                cost (int): amount the drink costs
            returns:
                Boolean: True or False
        """
        pay_with = input("Would you like to pay with card or cash? ").lower()
        if pay_with == 'cash':
            self.process_cash()
            if self.money_received >= cost:
                change = round(self.money_received - cost, 2)
                print(f"Here is {self.CURRENCY}{change} in change.")
                self.profit += cost
                self.money_received = 0
                return True
            else:
                print("Sorry that's not enough money. Money refunded.")
                self.money_received = 0
                return False
        else:
            self.profit += round(cost, 2)
            self.card_company_payment += round(cost * .02, 2)
            self.money_received = 0
            return True
