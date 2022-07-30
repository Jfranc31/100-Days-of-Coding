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
        print(f"Money: {self.CURRENCY}" + str("%.2f" % round(self.profit, 2)))
        print(f"Card Company Payment: {self.CURRENCY}" + str("%.2f" % round(self.card_company_payment, 2)))

    def process_cash(self, cost):
        """
        Returns the total calculated from dollars inserted.
            returns:
                self.money_received (int): Amount of money user inputted in total
        """
        print("Please insert dollars.")
        for dollar in self.DOLLAR_VALUES:
            self.money_received += int(input(f"How many {dollar}?: ")) * self.DOLLAR_VALUES[dollar]
            if self.money_received >= 5 and self.money_received >= cost:
                break
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
            self.process_cash(cost)
            if self.money_received >= cost:
                change = round(self.money_received - cost, 2)
                print(f"Here is {self.CURRENCY}" + str("%.2f" % round(change, 2)) + " in change.")
                self.profit += cost
                self.money_received = 0
                return True
            else:
                print("Sorry that's not enough money. Money refunded.")
                self.money_received = 0
                return False
        elif pay_with == 'card':
            self.profit += round(cost, 2)
            self.card_company_payment += round(cost * .02, 2)
            self.money_received = 0
            return True
