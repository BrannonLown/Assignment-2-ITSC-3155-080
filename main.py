import data
from sandwich_maker import SandwichMaker
from cashier import Cashier
from sandwich_maker import SandwichMaker
from cashier import Cashier

# Make an instance of other classes here
resources = data.resources
recipes = data.recipes
sandwich_maker_instance = SandwichMaker(resources)
cashier_instance = Cashier()




def main():
    ###  write the rest of the codes ###
    while True:
        user_input = input("What would you like? (small/ medium/ large/ off/ report): ")
        if user_input == "off":
            break
        if user_input == "report":
            print(f"Bread: {resources['bread']} slice(s)")
            print(f"Ham: {resources['ham']} slice(s)")
            print(f"Cheese: {resources['cheese']} pound(s)")
        if user_input == "small" or user_input == "medium" or user_input == "large":
            if sandwich_maker_instance.check_resources(recipes[user_input]["ingredients"]):
                if cashier_instance.transaction_result(recipes[user_input]["cost"], cashier_instance.process_coins()):
                    sandwich_maker_instance.make_sandwich(user_input, recipes[user_input]["ingredients"])
        else:
            print("Not an option, try again.")


if __name__=="__main__":
    main()
