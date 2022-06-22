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
money = 0
resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}


def payment_process():
    print(f"Please insert coins.")
    total  = (int(input("How many quarters?"))) * 0.25
    total += (int(input("How many dimes?"))) * 0.1
    total += (int(input("How many nickles?"))) * 0.05
    total += (int(input("How many pennies?"))) * 0.01
    return total
    # price = MENU[coffee]["cost"]
    # change = 0


def check(order_ingredients):
    for item in order_ingredients:
        if order_ingredients[item] > resources[item]:
            print(f"Sorry not enough {item}")
            return False
    return True


def is_transaction_successful(money_received, drink_cost):
    if money_received >= drink_cost:
        change = round(money_received - drink_cost, 2)
        print(f"Here is ${change} in change.")
        global money
        money += drink_cost
        return True
    else:
        print("Sorry that's not enough money. Money refunded.")
        return False


def make_coffee(drink_name, order_ingredients):
    for item in order_ingredients:
        resources[item] -= order_ingredients[item]
    print(f"Here is your {drink_name}. Enjoy!")


is_machine_finished = False
while not is_machine_finished:
    coffee = input('Prompt user by asking “What would you like? (espresso/latte/cappuccino): ').lower()
    if coffee == "report":
        print(f"Water: {resources['water']}ml")
        print(f"Milk: {resources['milk']}ml")
        print(f"Coffee: {resources['coffee']}g")
        print(f"Money: ${money}")
    elif coffee == 'off':
        is_machine_finished = True
    else:
        drink = MENU[coffee]
        if check(drink['ingredients']):
            payment = payment_process()
            if is_transaction_successful(payment, drink['cost']):
                make_coffee(coffee, drink['ingredients'])

# quarters = dimes = nickles = pennies = 0

