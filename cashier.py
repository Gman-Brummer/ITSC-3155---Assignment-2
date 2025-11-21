### Cashier ###

class Cashier:
    COIN_VALUES = {
        "quarters": 0.25,
        "dimes": 0.10,
        "nickels": 0.05,
        "pennies": 0.01,
    }

    def process_coins(self):
        """Returns total money inserted."""
        print("Please insert coins.")
        total = 0

        for coin in self.COIN_VALUES:
            count = int(input(f"How many {coin}? "))
            total += count * self.COIN_VALUES[coin]

        return round(total, 2)

    def transaction_result(self, money_received, drink_cost):
        """Return True if payment accepted, False if not."""
        if money_received < drink_cost:
            print("Sorry, that's not enough money. Money refunded.")
            return False

        change = round(money_received - drink_cost, 2)
        if change > 0:
            print(f"Here is ${change} in change.")

        print("Payment successful.")
        return True

