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

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}


def generate_report(money):
    print(f"Water: {resources['water']}ml")
    print(f"Milk: {resources['milk']}ml")
    print(f"Coffee: {resources['coffee']}g")
    print(f"Money: ${money}")


def coin_sum_check(coffee_price):
    print("Please insert coins.")
    cents25 = int(input("How many quarters?: "))
    cents10 = int(input("How many dimes?: "))
    cents5 = int(input("How many nickels?: "))
    cent = int(input("How many pennies?: "))
    user_coin_sum = cents25 * 0.25 + cents10 * 0.1 + cents5 * 0.05 + cent * 0.01
    return user_coin_sum


def get_coffee_price(coffee_type):
    return MENU[coffee_type]["cost"]


def ingredients_check(coffee_type):
    if resources["water"] < MENU[coffee_type]["ingredients"]["water"]:
        return "water"
    elif coffee_type != "espresso" and resources["milk"] < MENU[coffee_type]["ingredients"]["milk"]:
        return "milk"
    elif resources["coffee"] < MENU[coffee_type]["ingredients"]["coffee"]:
        return "coffee"
    else:
        return 0


def make_coffee(coffee):
    resources["water"] -= MENU[coffee]["ingredients"]["water"]
    resources["coffee"] -= MENU[coffee]["ingredients"]["coffee"]
    if coffee != "espresso":
        resources["milk"] -= MENU[coffee]["ingredients"]["milk"]


def coffee_machine():
    money = 0
    while True:
        coffee = input("What would you like?(espresso/latte/cappuccino): ").lower()
        if coffee == "report":
            generate_report(money)
        else:
            coffee_ingredients = ingredients_check(coffee)
            if coffee_ingredients == 0:
                coffee_price = get_coffee_price(coffee)
                coin_sum = coin_sum_check(coffee_price)
                balance = round(coin_sum - coffee_price,2)
                if balance < 0:
                    print("Sorry that's not enough money. Money refunded.")
                else:
                    make_coffee(coffee)
                    money += coffee_price
                    print(f"Here is ${balance} in change.")
                    print(f"Here is your {coffee} ☕ Enjoy!")
            else:
                print(f"Sorry, there is not enough {coffee_ingredients}.")


coffee_machine()
