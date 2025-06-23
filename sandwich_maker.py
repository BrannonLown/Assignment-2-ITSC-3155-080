
class SandwichMaker:
    def __init__(self, resources):
        self.machine_resources = resources

    def check_resources(self, ingredients):
        """Returns True when order can be made, False if ingredients are insufficient."""
        for ingredient in ingredients:
            if ingredient not in self.machine_resources:
                print("This resource is not available")
                return False
            elif self.machine_resources[ingredient] < ingredients[ingredient]:
                print(f"Sorry there is not enough {ingredient}.")
                return False
        return True

    def make_sandwich(self, sandwich_size, order_ingredients):
        """Deduct the required ingredients from the resources.
           Hint: no output"""
        if self.check_resources(order_ingredients):
            for ingredient in self.machine_resources:
                self.machine_resources[ingredient] -= order_ingredients[ingredient]
            print(f"{sandwich_size} sandwich is ready! Bon appetit!")