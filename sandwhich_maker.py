### Sandwich Maker ###

class SandwichMaker:
    def __init__(self, resources):
        self.resources = resources

    def is_resource_sufficient(self, order_ingredients):
        """Returns True if ingredients are available, otherwise False."""
        for item in order_ingredients:
            if order_ingredients[item] > self.resources[item]:
                print(f"Sorry, there is not enough {item}.")
                return False
        return True

    def make_sandwich(self, sandwich_size, order_ingredients):
        """Deduct ingredients from resources and make the sandwich."""
        for item in order_ingredients:
            self.resources[item] -= order_ingredients[item]
        print(f"Here is your {sandwich_size} ham sandwich! Enjoy!")
   