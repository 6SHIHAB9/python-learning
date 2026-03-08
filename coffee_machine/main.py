MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "milk": 0,
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

Money= 0

def ask_money():
    print("please insert coins.")
    quarters = int(input("how many quarters?: "))
    dimes = int(input("how many dimes?: "))
    nickles = int(input("how many nickles?: "))
    pennies = int(input("how many pennies?: "))

    money_received = (quarters * 0.25) + (dimes * 0.10) + (nickles * 0.05) + (pennies * 0.01)
    return money_received

def resource_management(inventory,milk_required,water_required,coffee_required):
    inventory["milk"] -= milk_required
    inventory["water"] -= water_required
    inventory["coffee"] -= coffee_required
    return inventory





while True:
    choice = input("What would you like? (espresso/latte/cappuccino): ")

    if choice == "off":
        break
    elif choice == "report":
        print(f"""Water : {resources["water"]}
Milk : {resources["milk"]}
Coffee: {resources["coffee"]},
Money: ${Money}""")
        continue
    elif choice == "latte" or choice == "espresso" or choice ==  "cappuccino":
        if MENU[choice]["ingredients"]["water"] > resources["water"] or MENU[choice]["ingredients"]["milk"] > resources["milk"] or MENU[choice]["ingredients"]["coffee"] > resources["coffee"]:
            print("Sorry there is not enough materials.")
            continue
    else:
        print("Please Enter a valid option!!")
        continue

    money_got = ask_money()
    if money_got < MENU[choice]["cost"]:
        print("Sorry that's not enough money. Money refunded.")
        continue
    elif money_got > MENU[choice]["cost"]:
        change = money_got - MENU[choice]["cost"]
        print(f"Here is ${change:.2f} dollars in change")

    resource_management(resources, MENU[choice]["ingredients"]["milk"], MENU[choice]["ingredients"]["water"], MENU[choice]["ingredients"]["coffee"])
    Money += MENU[choice]["cost"]

    print(f"Here is your {choice}.Enjoy!")



