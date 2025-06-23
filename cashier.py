class Cashier:
    def __init__(self):
        pass

    def process_coins(self):
        """Returns the total calculated from coins inserted.
           Hint: include input() function here, e.g. input("how many quarters?: ")"""
        dollars = int(input("How many dollars?: "))
        half_dollars = int(input("How many half-dollars?: "))
        quarters = int(input("How many quarters?: "))
        nickels = int(input("How many nickels?: "))
        total = dollars + half_dollars*0.5 + quarters*0.25 + nickels*0.05
        return total

    def transaction_result(self, coins, cost):
        """Return True when the payment is accepted, or False if money is insufficient.
           Hint: use the output of process_coins() function for cost input"""
        if coins <= cost:
            change = cost - coins
            print(f"Here is ${change} in change")
            return True
        else:
            print("Sorry that is not enough money. Money refunded.")
            return False
