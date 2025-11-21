### Main Program ###

import data
from sandwhich_maker import SandwichMaker
from cashier import Cashier

# Setup
resources = data.resources
recipes = data.recipes

sandwich_maker = SandwichMaker(resources)
cashier = Cashier()

machine_on = True

while machine_on:
    print("\nWhat would you like? (small/medium/large)")
    user_choice = input("Enter choice or 'report' or 'off': ").lower()

    match user_choice:
        case "off":
            print("Turning off machine...")
            machine_on = False

        case "report":
            print("\n--- Machine Report ---")
            print(f"Bread: {resources['bread']} slices")
            print(f"Ham: {resources['ham']} slices")
            print(f"Cheese: {resources['cheese']} oz")
            print(f"Money: ${resources['money']}")
            print("----------------------")

        case "small" | "medium" | "large":
            sandwich = recipes[user_choice]
            ingredients = sandwich["ingredients"]
            cost = sandwich["cost"]

            if sandwich_maker.is_resource_sufficient(ingredients):
                payment = cashier.process_coins()
                if cashier.transaction_result(payment, cost):
                    resources["money"] += cost
                    sandwich_maker.make_sandwich(user_choice, ingredients)

        case _:
            print("Invalid selection. Try again.")
