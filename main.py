MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}
# TODO: 1. print report  of all coffee machine resources
profit = 0
resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}


def is_resource_sufficient(oder_ingredients):
    """Returns True when order can be made, False if ingredients are insuffficient"""
    for item in oder_ingredients:
        if oder_ingredients[item] >= resources[item]:
            print(f"Sorry there is not enough {item}.")
            return False

    return True


def process_coins():
    """Returns the calculated from coins inserted"""
    print("Please insert some coins")
    total = int(input("how many quarters?: ")) * 0.25
    total += int(input("how many dimes?: ")) * 0.1
    total += int(input("how many nickels?: ")) * 0.05
    total += int(input("how many pennies?: ")) * 0.01
    return total

def is_transaction_succeesful(money_received, drink_cost):
    """Return True when the payment is accepted, or False if money is insufficient."""
    if money_received >= drink_cost:
        change = round(money_received - drink_cost, 2)
        print(f"Here is ${change} in change.")
        global profit
        profit += drink_cost
        return True
    else:
        print("Sorry that's not enough money. Money refunded")
        return False

def make_coffee(drink_name, order_ingredients):
    """Deduct the required ingredients form the resources"""
    for item in order_ingredients:
        resources[item] -= order_ingredients[item]
    print(f"Here is your {drink_name}☕! Enjoy")



is_on = True

while is_on:
    choice = input("what would you like to have? (espresso/latte/capuchino): ")
    if choice == "off":
        is_on = False
    elif choice == "report":
        print(f"Water: {resources['water']}ml")
        print(f"milk: {resources['milk']}ml")
        print(f"coffee:{resources['coffee']}gr")
        print(f"Money: ${profit}")

    else:
        drink = MENU [choice]
        if is_resource_sufficient(drink["ingredients"]):
            payment = process_coins()
            if is_transaction_succeesful(payment, drink["cost"]):
                make_coffee(choice, drink["ingredients"])