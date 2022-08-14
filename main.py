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
profit = 0
resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}


# TODO: 4.Check resources sufficient?
def check_resources(other_ingredients):
    for item in other_ingredients:
        if other_ingredients[item] >= resources[item]:
            print(f"Sorry there is not enough {item}.")
            return False
    return True


def process_coin():
    print("Please Insert Coins")
    total = int(input("How many quarters? ")) * 0.25
    total += int(input("How many dimes? ")) * 0.1
    total += int(input("How many nickels? ")) * 0.05
    total += int(input("How many pennies? ")) * 0.01
    return total


def check_transaction(money_received, drink_cost):
    if money_received >= drink_cost:
        change = round((money_received - drink_cost),2)
        print(f"Here is ${change} dollars in change.")
        global profit
        profit += drink_cost
        return True
    else:
        print("Sorry that's not enough money. Money refunded.")
        return False


def make_coffee(drink_name, other_ingredients):
    for item in other_ingredients:
        resources[item] -= other_ingredients[item]
    print(f"Here is your {drink_name}.Enjoy! ☕")


is_on = True
while is_on:
    # TODO: 1.Prompt user by asking “What would you like? (espresso / latte / cappuccino):”
    choice = input("What would you like? (espresso/latte/cappuccino): ")
    # TODO: 2.Turn off the Coffee Machine by entering “off” to the prompt.
    if choice == "off".lower():
        is_on = False
    # TODO: 3. Print report.
    elif choice == "report":
        print(f"Water: {resources['water']}ml")
        print(f"Milk: {resources['milk']}ml")
        print(f"Coffee: {resources['coffee']}g")
        print(f"Money: ${profit}")
    else:
        drink = MENU[choice]
        if check_resources(drink["ingredients"]):
            payment = process_coin()
            if check_transaction(payment, drink["cost"]):
                make_coffee(choice, drink["ingredients"])



